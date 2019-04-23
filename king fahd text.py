# this program will download the text from King Fahd Complex
# text can be used in conjuction with QCF fonts
# http://quran.qurancomplex.gov.sa/Quran/display/qrn_page.asp?nAya=1&nSora=1&l=eng&r=1&ServerToken=http%3A%2F%2Fquran%2Equrancomplex%2Egov%2Esa&ref=1

import html
import urllib.request
import re

header = 'Surah Number,Surah Name,Ayah Number,Ayah Text (decoded),Ayah Text (encoded),Page'
file = open('quran.txt','w+',  encoding='utf-8')
file.write(str(header))
file.close()

suwar = ['al-Fatihah', 'al-Baqarah', 'Alee \'Imran', 'an-Nisa', 'al-Ma\'idah', 'al-An\'am', 'al-A\'raf', 'al-Anfal', 'at-Tawbah', 'Yunus', 'Hud', 'Yusuf', 'ar-Ra\'d', 'Ibrahim', 'al-Hijr', 'an-Nahl', 'al-Isra', 'al-Kahf', 'Maryam', 'Taha', 'al-Anbya', 'al-Haj', 'al-Mu\'minun', 'an-Nur', 'al-Furqan', 'ash-Shu\'ara', 'an-Naml', 'al-Qasas', 'al-\'Ankabut', 'ar-Rum', 'Luqman', 'as-Sajdah', 'al-Ahzab', 'Saba', 'Fatir', 'Ya-Sin', 'as-Saffat', 'Sad', 'az-Zumar', 'Ghafir', 'Fussilat', 'ash-Shuraa', 'az-Zukhruf', 'ad-Dukhan', 'al-Jathiyah', 'al-Ahqaf', 'Muhammad', 'al-Fath', 'al-Hujurat', 'Qaf', 'adh-Dhariyat', 'at-Tur', 'an-Najm', 'al-Qamar', 'ar-Rahman', 'al-Waqi\'ah', 'al-Hadid', 'al-Mujadila', 'al-Hashr', 'al-Mumtahanah', 'as-Saf', 'al-Jumu\'ah', 'al-Munafiqun', 'at-Taghabun', 'at-Talaq', 'at-Tahrim', 'al-Mulk', 'al-Qalam', 'al-Haqqah', 'al-Ma\'arij', 'Nuh', 'al-Jinn', 'al-Muzzammil', 'al-Muddaththir', 'al-Qiyamah', 'al-Insan', 'al-Mursalat', 'an-Naba', 'an-Nazi\'at', '\'Abasa', 'at-Takwir', 'al-Infitar', 'al-Mutaffifin', 'al-Inshiqaq', 'al-Buruj', 'at-Tariq', 'al-A\'la', 'al-Ghashiyah', 'al-Fajr', 'al-Balad', 'ash-Shams', 'al-Layl', 'ad-Duhaa', 'ash-Sharh', 'at-Tin', 'al-\'Alaq', 'al-Qadr', 'al-Bayyinah', 'az-Zalzalah', 'al-\'Adiyat', 'al-Qari\'ah', 'at-Takathur', 'al-\'Asr', 'al-Humazah', 'al-Fil', 'Quraysh', 'al-Ma\'un', 'al-Kawthar', 'al-Kafirun', 'an-Nasr', 'al-Masad', 'al-Ikhlas', 'al-Falaq', 'an-Nas']

ayaat = [7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135, 112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6]

# open text file and append
file = open('quran.txt','a+',  encoding='utf-8')

for s_index, a_index in enumerate(ayaat):
	for ayah in range(a_index):
		parser = 'onclick=ClickAyaArea(' + str(int(s_index+1)) + ',' + str(int(ayah+1)) + ') target=_top>'
		url = 'http://quran.qurancomplex.gov.sa/Quran/display/qrn_page.asp?nAya=' + str(int(ayah+1)) + '&nSora=' + str(int(s_index+1)) + '&l=eng&r=1&ServerToken=http%3A%2F%2Fquran%2Equrancomplex%2Egov%2Esa&ref=1'
		quran_pg_req = urllib.request.Request(url)
		quran_pg_resp = urllib.request.urlopen(quran_pg_req)
		quran_pg_data = quran_pg_resp.read()
		ayah_txt_html = re.findall(r'' + re.escape(parser) + '(.*?)</A>', str(quran_pg_data))
		ayah_txt_encoded = ''.join(ayah_txt_html)
		ayah_txt_decoded = html.unescape(ayah_txt_encoded)
		pg_parser = 'sc_F0 {FONT-FAMILY:QCF_P'
		pg = re.findall(r'' + re.escape(pg_parser) + '(.*?)\;', str(quran_pg_data))
		verse = str(int(s_index+1)) + ',Surah ' + suwar[s_index] + ',' + str(int(ayah+1)) + ',' + str(ayah_txt_decoded) + ',' + str(ayah_txt_encoded) + ',' + str(pg[0])
		file.write('\n' + verse)

file.close()

print('fin')