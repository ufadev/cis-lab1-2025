#!/usr/bin/env python3
"""
Конвертер TRX (Visual Studio Test Results) в формат Allure
"""
import xml.etree.ElementTree as ET
import json
import os
import sys
from datetime import datetime
import uuid

def parse_trx_to_allure(trx_file, output_dir):
    """Конвертирует TRX файл в формат Allure JSON"""
    if not os.path.exists(trx_file):
        print(f"TRX file not found: {trx_file}")
        return
    
    tree = ET.parse(trx_file)
    root = tree.getroot()
    
    # Namespace для TRX
    ns = {'': 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'}
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Получаем все тесты
    test_definitions = {}
    for test in root.findall('.//TestDefinition', ns):
        test_id = test.get('id')
        test_name = test.find('.//TestMethod', ns)
        if test_name is not None:
            test_definitions[test_id] = {
                'name': test_name.get('name', 'Unknown'),
                'classname': test_name.get('className', 'Unknown')
            }
    
    # Обрабатываем результаты
    for i, result in enumerate(root.findall('.//UnitTestResult', ns)):
        test_id = result.get('testId')
        test_def = test_definitions.get(test_id, {'name': 'Unknown', 'classname': 'Unknown'})
        
        test_name = test_def['name']
        outcome = result.get('outcome', 'Unknown')
        duration_str = result.get('duration', '00:00:00.0000000')
        
        # Парсим duration
        duration_ms = 0
        try:
            parts = duration_str.split(':')
            if len(parts) == 3:
                hours = int(parts[0])
                minutes = int(parts[1])
                seconds = float(parts[2])
                duration_ms = int((hours * 3600 + minutes * 60 + seconds) * 1000)
        except:
            pass
        
        status = 'passed' if outcome == 'Passed' else 'failed'
        
        # Получаем сообщение об ошибке если есть
        error_message = None
        error_trace = None
        std_out = result.find('.//Output', ns)
        if std_out is not None:
            error_info = std_out.find('.//ErrorInfo', ns)
            if error_info is not None:
                error_message = error_info.find('.//Message', ns)
                error_trace = error_info.find('.//StackTrace', ns)
                if error_message is not None:
                    error_message = error_message.text
                if error_trace is not None:
                    error_trace = error_trace.text
        
        # Создаем Allure result
        allure_result = {
            "uuid": str(uuid.uuid4()),
            "name": test_name,
            "fullName": f"{test_def['classname']}.{test_name}",
            "historyId": str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{test_def['classname']}.{test_name}")),
            "status": status,
            "time": {
                "start": int(datetime.now().timestamp() * 1000) - duration_ms,
                "stop": int(datetime.now().timestamp() * 1000),
                "duration": duration_ms
            },
            "labels": [
                {"name": "suite", "value": test_def['classname']},
                {"name": "testClass", "value": test_def['classname']},
                {"name": "package", "value": test_def['classname']}
            ]
        }
        
        if error_message:
            allure_result["statusDetails"] = {
                "message": error_message,
                "trace": error_trace or ""
            }
        
        # Сохраняем результат
        output_file = os.path.join(output_dir, f"{i}-result.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(allure_result, f, indent=2, ensure_ascii=False)
        
        print(f"Converted: {test_name} -> {status}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: convert_trx_to_allure.py <trx_file> <output_dir>")
        sys.exit(1)
    
    trx_file = sys.argv[1]
    output_dir = sys.argv[2]
    parse_trx_to_allure(trx_file, output_dir)

