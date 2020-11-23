import os
import sys
import json
import jsonschema
from jsonschema import validate
import re

#os.chdir('C:\\Рабочая_2020\\IT_education\\Welltory\\task_folder')
base_folder = os.getcwd()

schema_dirpath = base_folder + '\\schema\\'
json_dirpath = base_folder + '\\event\\'

os.chdir(schema_dirpath)
list_jsonschema = os.listdir(os.getcwd())

os.chdir(json_dirpath)
list_jsonfile = os.listdir(os.getcwd())

#num_f = int(input('Введите номер файла'))

for json_file in list_jsonfile:
    fname = json_dirpath + json_file
    with open(fname, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

    log_name = json_file[0:len(json_file)-5] + '.log'
    os.chdir(base_folder)

    if type(data) == type(dict()) and len(data) != 0:
        with open(log_name, 'w') as file_wr:
            file_wr.write('json - ' + ' ' + json_file + '\n')
            print('json - ', json_file)
            for i in range(4):
                num_sch = i
                sname = schema_dirpath + list_jsonschema[num_sch]
                with open(sname, 'r', encoding='utf-8-sig') as file:
                    schema = json.load(file)
    
                try:
                    jsonschema.Draft7Validator.check_schema(schema)
                except jsonschema.exceptions.SchemaError as e:
                    print('The schema is invalid', e)
    

                eldata_lst = []
                elschema_lst = []
                elerror_lst = []
                elerror_lst1 = []
                full_dict = {}
                log_lst = []

                v = jsonschema.Draft7Validator(schema)
                errors = sorted(v.iter_errors(data), key=lambda e: e.path)
        
        
                try:
                    for el in data:
                        eldata_lst.append(el)
                except Exception as e:
                    print(e)
                for el in schema['properties']:
                    elschema_lst.append(el)
                for error in errors:
                    els_str = ''
                    for el in error.schema_path:
                        els_str = els_str + ' ' + "'" + el + "'"
                    els_str = els_str + ' ' + error.message
                    elerror_lst.append(els_str)

                lst = eldata_lst + elschema_lst
        
                for el in lst:
                    full_dict[el] = ['', '', '', '', '']

                for el in full_dict:
                    if el in eldata_lst:
                        if el in elschema_lst:
                            full_dict[el][0] = 'in everywhere'
                        else:
                            full_dict[el][0] = 'in json {root}'
                    else:
                        if el in elschema_lst:
                            full_dict[el][0] = 'in schema {proper}'
                    for ele in elerror_lst:
                        if ("'"+el+"'") in ele:
                            full_dict[el][4] = ele
        
        
                for el in data:
                    if type(data[el]) == type(dict()):
                        for elem in data[el]:
                            if elem in full_dict:
                                full_dict[elem][2] = 'in json {{"{}" {{}} }}'.format(el)
                        
        
                for el in full_dict:
                    if full_dict[el][0] == 'in everywhere' and full_dict[el][4] == '':
                        full_dict[el][1] = 'Valid'
                    else:
                        if full_dict[el][0] == 'in json {root}':
                            full_dict[el][1] = 'Invalid'
                        else:
                            if full_dict[el][0] == 'in everywhere' and full_dict[el][4] != '':
                                full_dict[el][1] = 'Invalid'
                            else:
                                full_dict[el][1] = ''
                    if full_dict[el][1] == 'Invalid' and full_dict[el][2] == '' and full_dict[el][4] == '':
                        full_dict[el][3] = 'ADD the field in the schema or REMOVE field'
                    if full_dict[el][2] != '':
                        full_dict[el][3] = 'MOVE the field to the json {root} '
            
                    if full_dict[el][4] != '':
                        full_dict_el4 = re.findall(r"['](\w+)[']", str(full_dict[el][4]))
                        if full_dict_el4[0] == 'required':
                            if full_dict[el][2] != '':
                                full_dict[el][3] = 'MOVE the required field to the json {root}'
                            else:
                                full_dict[el][3] = 'ADD the required fiels in the json {root}'
                        else:
                            if full_dict_el4[0] == 'properties':
                                full_dict[el][3] = full_dict[el][3] + 'CONTROL type or limits of the field'

            
                print('')
        
                print('schema - ', list_jsonschema[num_sch])
                print('')
                print('FIELD NAME'.center(17,'.'), 'LOCATION'.center(20,'.'), 'VALIDITY'.center(10,'.'), 
                      'YOU CAN FIND FIELD'.center(25,'.'), 'RECOMENDATIONS'.center(40,'.'))
                print('')
                for el in full_dict:
                    print(el.ljust(17,'.'), full_dict[el][0].ljust(20,'.'), full_dict[el][1].ljust(10,'.'), 
                          full_dict[el][2].ljust(25,'.'), full_dict[el][3].ljust(40,'.'))
            
                file_wr.write('\n')
        
                file_wr.write('schema - ' + ' ' + list_jsonschema[num_sch] + '\n')
                file_wr.write('\n')
                file_wr.write('FIELD NAME'.center(17,'.') + '|' + 'LOCATION'.center(20,'.') + '|' + 'VALIDITY'.center(10,'.')+ '|' + 
                      'YOU CAN FIND FIELD'.center(25,'.') + '|' + 'RECOMENDATIONS'.center(40,'.') + '\n')
                file_wr.write('\n')
                for el in full_dict:
                    file_wr.write(el.ljust(17,'.') + '|' + full_dict[el][0].ljust(20,'.') + '|' + full_dict[el][1].ljust(10,'.') + '|' + 
                          full_dict[el][2].ljust(25,'.') + '|' + full_dict[el][3].ljust(40,'.') + '\n')
        
    else:
        print('Json {} is empty.'.format(json_file))
        print(data)
        with open(log_name, 'w') as file_wr:
            file_wr.write('Json {} is empty.'.format(json_file) + '\n')
            file_wr.write('File contains: ' + str(data))
