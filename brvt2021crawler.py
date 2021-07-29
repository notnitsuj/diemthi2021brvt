from bs4 import BeautifulSoup
from selenium import webdriver
import csv

# Set up variables
chrome_path = 'chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=0)
url = 'https://thanhnien.vn/giao-duc/tuyen-sinh/2021/tra-cuu-diem-thi-thpt-quoc-gia.html'
driver.get(url)
diemthi = []

# Loop through all students
for sbd in range (52000001, 52013196):
    # Enter ID
    description = driver.find_element_by_id('txtkeyword')
    description.clear()
    description.send_keys(sbd, webdriver.common.keys.Keys.ENTER)

    # Page source
    html = driver.page_source
    page = BeautifulSoup(html, 'lxml')

    # Extract grades
    rows = page.find('tbody', {'id': 'resultcontainer'}).findAll('tr')
    for row in rows:
        monthi = row.findAll('td')
        diem = {}
        if (len(monthi) == 18):
            diem['SBD'] = monthi[3].text
            diem['Toan'] = monthi[6].text
            diem['Van'] = monthi[7].text
            diem['Ly'] = monthi[8].text
            diem['Hoa'] = monthi[9].text
            diem['Sinh'] = monthi[10].text
            diem['Su'] = monthi[12].text
            diem['Dia'] = monthi[13].text
            diem['GDCD'] = monthi[14].text
            diem['Anh'] = monthi[16].text
            diemthi.append(diem.copy())

# End session
driver.quit()
print('Finished.')

# Export as csv
keys = diemthi[0].keys()
a_file = open("diemthi.csv", "w")
dict_writer = csv.DictWriter(a_file, keys)
dict_writer.writeheader()
dict_writer.writerows(diemthi)
a_file.close()