import yaml
import os

filePath = os.path.dirname(__file__)
print(filePath)
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
print(fileNamePath)
yamlPath = os.path.join(fileNamePath,'config.yaml')
print(yamlPath)
f = open(yamlPath,'r',encoding='utf-8')
cont = f.read()
yl = yaml.load(cont)
#y2 = yaml.dump(cont)
#print(x)
#print(yl['test_login']['Ua_input'])
#print(yl.get('test_login'))

#print(yl.get('Ua_input'))
print(yl)
#print(yl['test_login']['LA'])
print(yl['test_lk']['LA'])