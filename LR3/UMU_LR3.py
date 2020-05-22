from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#ЛР1
file = open('data.csv')
#Раздел "Парсинг"
#объявляем необходимые переменные
msisdn_origin = 0
msisdn_dest = 0
call_durationISH = 0
call_durationVH = 0
sms_number = 0
i = 0
t = 0
#получаем все строки в виде списка
l = file.readlines()
#получаем кол-во строк
s = len(l)
#выбираем нужные строки и данные CDR; проходимся по спискам l и создаём подсписки
for i in range(s):
    x = l[i].split(',')
#получаем длину подсписка
    y = len(x)
#выбираем нужные нам строки и данные CDR
    for t in range(y):
        if x[t] == '915642913' and len(x[t - 1]) != 9:
            msisdn_origin = x[t]
            msisdn_dest = x[t+1]
            call_durationISH = x[t+2]
        if x[t] == '915642913' and len(x[t - 1]) == 9:
            call_durationVH = x[t+1]
            sms_number = x[t+2]
#Раздел "Тарификация"
call_duration = 0
X = 0
k = 1
T = 0
#тарификация Телефонии
T = float(call_durationISH) + float(call_durationVH)
X = T * k
Y = 0
kSMS = 1
freeSMS = 5
N = int(sms_number)
#тарификация СМС
Y = (N - freeSMS) * kSMS
print('Итоговая стоимость звонков абонента 915642913 за текущий период:', X, 'руб.')
print('Итоговая стоимость СМС абонента 915642913 за текущий период:', Y, 'руб.')

#ЛР2
file = open('data2.csv')
l2 = file.readlines()
s2 = len(l2)
#объявляем необходимые переменные
sum = 0
z = 0
b = 0
u = 0
bM = 0
sumb = 0
sumbM = 0
m = []
n = []
#парсинг нужных данных
for j in range(s2):
    x2 = l2[j].split(',')
    u = x2[2].split('.')
    y2 = x2[4].split(':')
    z = x2[8]
    if y2[0] == '192.168.250.59':
        m.append(u[0])
        n.append(x2[8])
        if z.isdigit():
            b = int(z)
            sumb = sumb + b
        else:
            bM = float(z) * 1048576
            sumbM = sumbM + bM
sum = sumb + sumbM
#подсчёт итоговой стоимости
X2 = float('{:.2f}'.format(((sum - 1000) / 1048576) * 1))
print('Для абонента с IP-адресом 192.168.250.59 и коэффициентом k: 1руб/Мб, учитывая, что первые 1000б бесплатно итоговая стоимость интернета:', X2, 'руб.')

#ЛР3
#создать новый PDF с пом. Reportlab
packet = io.BytesIO()
#добавление информации
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Courier', 10)
can.drawString(82, 720, "Svetlov A. D.")
can.drawString(55, 755, "566766834")
can.drawString(195, 755, "568901094")
can.drawString(100, 767, "SberBank")
can.drawString(352, 755, "002")
can.drawString(352, 780, "001")
can.drawString(352, 792.5, "123123")
can.drawString(100, 644, "SkyNet")
can.drawString(81, 610, "Svetlov A. D.")
can.drawString(83, 585, "-")
can.drawString(65, 550, "Telephony")
can.drawString(65, 535, "SMS")
can.drawString(65, 520, "Internet")
can.drawString(43, 535, "2")
can.drawString(43, 520, "3")
can.drawString(335, 550, "1    1")
can.drawString(335, 520, "1    1")
can.drawString(335, 535, "1    1")
can.drawString(405, 550, str(X))
can.drawString(405, 520, str(X2))
can.drawString(405, 535, str(Y))
can.drawString(480, 550, str(X))
can.drawString(480, 520, str(X2))
can.drawString(480, 535, str(Y))
can.drawString(444, 496, str(X + Y + X2))
can.drawString(444, 484, str(float('{:.2f}'.format(1.2*(X + Y + X2)))))
can.drawString(444, 471, str(float('{:.2f}'.format(1.2*(X + Y + X2)))))
can.drawString(128, 456, "3")
can.drawString(120, 342, "Sit E. A.")
can.drawString(395, 342, "Gill M. A.")
can.setFont('Times-Roman', 15)
can.drawString(160, 688, "1")
can.drawString(198, 688, "01.01.")
can.drawString(250, 688, "20")
can.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)
#читаем PDF
existing_pdf = PdfFileReader(open("input.pdf", "rb"))
output = PdfFileWriter()
#добавлениея водяного знака
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
#записываем новый PDF
outputStream = open("output.pdf", "wb")
output.write(outputStream)
outputStream.close()