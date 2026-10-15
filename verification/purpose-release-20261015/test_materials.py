from pathlib import Path
import json,base64,io,tempfile,sys,zipfile,subprocess
base=Path(r'E:\Github\omnara-deep-research\verification\purpose-apps-20261015')
source=Path(r'E:\Github\omnara-deep-research\workspace');sys.path.insert(0,str(source))
from work_io import Materials,select_home,config_file
home=Path(tempfile.mkdtemp(prefix='material-check-'));m=Materials(home,'omnara',source/'open.py','--data-root')
xml=b'<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>A real document paragraph about hinge contact.</w:t></w:r></w:p></w:body></w:document>'
b=io.BytesIO()
with zipfile.ZipFile(b,'w') as z:z.writestr('word/document.xml',xml)
r=m.handle('/api/material',{'name':'working-notes.docx','base64':base64.b64encode(b.getvalue()).decode()});assert 'hinge contact' in r['text']
from pypdf import PdfWriter
from pypdf.generic import DictionaryObject,NameObject,DecodedStreamObject
b=io.BytesIO();writer=PdfWriter();page=writer.add_blank_page(width=612,height=792);font=DictionaryObject({NameObject('/Type'):NameObject('/Font'),NameObject('/Subtype'):NameObject('/Type1'),NameObject('/BaseFont'):NameObject('/Helvetica')});page[NameObject('/Resources')]=DictionaryObject({NameObject('/Font'):DictionaryObject({NameObject('/F1'):writer._add_object(font)})});stream=DecodedStreamObject();stream.set_data(b'BT /F1 12 Tf 72 720 Td (The measured contact changed after the targeted repair.) Tj ET');page[NameObject('/Contents')]=writer._add_object(stream);writer.write(b)
r=m.handle('/api/material',{'name':'source.pdf','base64':base64.b64encode(b.getvalue()).decode()});assert 'targeted repair' in r['text']
try:m.handle('/api/material',{'path':str(home/'missing.docx')})
except ValueError as e:assert 'existing file' in str(e)
else:raise AssertionError('Missing source accepted')
root=m.handle('/api/browse',{'path':str(home)});assert root['path']==str(home)
import os
os.environ['CD_WORKSPACE_CONFIG']=str(home/'config');os.environ['LOCALAPPDATA']=str(home/'local')
selector=config_file('test');selector.parent.mkdir(parents=True);selector.write_text(str(home/'disconnected'))
fallback=select_home('test',home/'unused');assert fallback.exists() and (fallback/'.location-warning.txt').exists();assert not (home/'disconnected').exists()
(base/'material-results.json').write_text(json.dumps({'pass':True,'checks':['DOCX local extraction','PDF local extraction','missing source recovery message','source directory browse','missing remembered root falls back without creating false empty original']},indent=2))
for slug in ('signalhouse','promiseloop-creator-studio'):
 p=Path('E:/Github')/slug/'source/skills'/slug/'workspace/host.py';s=p.read_text();s=s.replace('from work_io import Materials, select_home','sys.dont_write_bytecode = True\nfrom work_io import Materials, select_home');p.write_text(s,encoding='utf-8',newline='\n')
print('PASS DOCX, PDF, missing source recovery, directory browse and unavailable remembered-root recovery')
