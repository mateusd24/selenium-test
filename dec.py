from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import undetected_chromedriver as uc
import pyautogui
import cv2
import numpy as np
import os
import random

import concurrent.futures

#https://www.zenrows.com/blog/undetected-chromedriver-vs-selenium-stealth#conclusion

"""
# Path to the target image in the same directory
target_image_path = os.path.join(os.getcwd(), 'on_button.png')
target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)

# Locate the image on the screen
screen = pyautogui.screenshot()
screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)

# Match template to locate the target image within the screenshot
result = cv2.matchTemplate(screen, target_image, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Set a threshold for match confidence
threshold = 0.8  # Adjust this value based on accuracy
if max_val >= threshold:
    x, y = max_loc
    # Center of the detected area
    x_center = x + target_image.shape[1] // 2
    y_center = y + target_image.shape[0] // 2

    print(f"Found image at (X, Y): ({x_center}, {y_center})")

    # Store the coordinates and optionally click on the location
    # Uncomment the following line if you want to perform the click:
    # pyautogui.click(x_center, y_center)
else:
    print("Image not found on the screen.")

"""





#breakpoint()




"""

import requests

cookies = {
    'cfid': 'b5b499fb-f741-47c9-a28c-8708324cafff',
    'cftoken': '0',
    '_ga': 'GA1.2.1196097370.1730816311',
    '_gid': 'GA1.2.554171955.1730816311',
    'Lyp1CWKh': 'AzjU-wOTAQAAh_TXlQyZcqC7cow2Fz8_URo2GhHk1plv9MiLLpBzHN8wdaYeAY5dRBGuct3FwH8AAEB3AAAAAA==',
    'TS01dc4fc6': '011101e881663f2f96553f3eab4070e06eb0f0f0d6fb210e69bef09fa6c37af96fd19dfda03cbd50aafd6121353cfd085e824f42ec',
    '_gat': '1',
    'OClmoOot': 'A5BPsPySAQAAnKA9yMVB-lGyLxzyi73k8IPssqSpqwqPoVv-gooQMuw75WeXAY5dTlKuct3FwH8AAEB3AAAAAA|1|0|e9424ed2798cb62e10150396a1d381cae16044ce',
    '000b03': 'YPvnYo+KI4Dayg+waa8PlsSGGvYS/oFNvVcqLeaYEN1iXM9ghs0GDuaeRI9xzmas1F6Oym1tNlkQpbvShIVr2c6NhkQrxYCkeAp5Es80Jb5dlvVoGHdmw3MwCN2GWpv+zJk/nNnTJOQ7FZn9G2LMgBV87asacFb8u67FMFWg1s8Y1uXK',
    '_ga_FJ2PMEKCDY': 'GS1.2.1730947796.5.1.1730947846.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cfid=b5b499fb-f741-47c9-a28c-8708324cafff; cftoken=0; _ga=GA1.2.1196097370.1730816311; _gid=GA1.2.554171955.1730816311; Lyp1CWKh=AzjU-wOTAQAAh_TXlQyZcqC7cow2Fz8_URo2GhHk1plv9MiLLpBzHN8wdaYeAY5dRBGuct3FwH8AAEB3AAAAAA==; TS01dc4fc6=011101e881663f2f96553f3eab4070e06eb0f0f0d6fb210e69bef09fa6c37af96fd19dfda03cbd50aafd6121353cfd085e824f42ec; _gat=1; OClmoOot=A5BPsPySAQAAnKA9yMVB-lGyLxzyi73k8IPssqSpqwqPoVv-gooQMuw75WeXAY5dTlKuct3FwH8AAEB3AAAAAA|1|0|e9424ed2798cb62e10150396a1d381cae16044ce; 000b03=YPvnYo+KI4Dayg+waa8PlsSGGvYS/oFNvVcqLeaYEN1iXM9ghs0GDuaeRI9xzmas1F6Oym1tNlkQpbvShIVr2c6NhkQrxYCkeAp5Es80Jb5dlvVoGHdmw3MwCN2GWpv+zJk/nNnTJOQ7FZn9G2LMgBV87asacFb8u67FMFWg1s8Y1uXK; _ga_FJ2PMEKCDY=GS1.2.1730947796.5.1.1730947846.0.0.0',
    'origin': 'https://appellatecases.courtinfo.ca.gov',
    'priority': 'u=0, i',
    'referer': 'https://appellatecases.courtinfo.ca.gov/search.cfm?dist=2&inputError=5',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

params = {
    'dist': '2',
    'search': 'number',
}

data = {
    'Xa4vrhYP3Q-a': 'TrQzTBL9B3m7_nvK5=68ius5D6giXotrXKRLUAwXltB6EI6a81XTwEN840FKTh1gwrdgdSubk7GyGW54vnYqBF1ZIoZRZOQx5=a=Swp1eDV=Z1dpuAihcGyGDlfrpFSt1RDe=R5dAv1_cdTZTrCmbjJ=iwuz1ezPgFDkbw023y4WFrzX6x28q8JrEJw9CkLrwPC57eRGcC63_TlDbBiFSyjym0q4gqXHYN98GAowLmwwa244ZsO78=nkDfCjuPyt95OEnQKmFYuqwbaoIvWF7opZfioxAGTpk0H3aLn4Fb-7aV3C9ahT1LitgS7_8m3LFa2yP3OBJ7vm26PHVwPhsByqKvmEV4tTUn3di005wCIAeZ5yNZ3tflCmSicBNmoFbCOD7q8DfYpc0QC5DNa8_WGUwWE1BcH9u_kOPN5yUiji1AcnWKT-_8l8EJ8YKIrstNrEHLdZuQVlDANGZprtpKEw8W=lQmQXIuWCbPTIk4TJjQdJJUQxNpWGNf1I70zZTkgJPbca5o9Su0Zq4cp2m3=cNz3a-IfbIfcRT3Rx4fDJ6G5RBhkXTLv_A1DILg_1LRd_q7F4jmGYAcbo_U91aJyChDd0=RtF6Lz2=dizY31DrE1kGfAXvvRbfz-bgqC4sw3JLXbTR7iixiwH60nPnyB8e-6IVbWisD_tnmpkUF9jOj8tao=LTF1YEoXHZiOuCnwFzEHabsfEaeD4z_eklyHzSeg6ALKBwycl5mgc7sg59CEcgX5LuiVaJDZld2lfb=PLphdH41q6x84NFnyr4V1Wb1_GSzr_YuXKPX-FHmemE_dGfno=PRG8mp5hlS7=PW6eWsejUsmNOQIY-4ZPsncvblBzg67WxwaLSfQwZGUpA-Nm32q3R9z5IHGApRTs=cUGaBA4yL7lsXOcZrj5cPzRx-USfPHwEU7QgQ7J-OVjeWullpjcFYnVLZNGHc=ziaIJtx0q1sUf5HauJkG8FOT8etbChnWxeZ3OjFLbrSYt-hH9Ss6k24kLhk=3I-bWXS-udW67Al2z9KqGqAHDNWhukUcem89SpwkG144lWa891GUDmj=PzB_mnydJqV81kizdZVhc_iX6kth1Aqrccq93O_BQF4Qb70NZ-4y3IChq53iEOGBnRcgfVU2syYGdOPOsuRAvBtnBCocldsQOws0O-lsKgdk5DuLTHn_gP=bY1fTeuxjXNKaex1=WcX1s4wqe1YSgi-9RVejIA3wlnrihstR27Tsxazzh1YOLYTJiQlKADmNcuiDKj7heurx0VnWcpWqH5mURs861Zqamc5C=bvTBbX94P=q7fiAFUn3tGBoAqzZOQKGKSq60JliS4Fqv3-3kjc7y9WCb0aKVQBlsqseDpuB_8y3YJQIE2Rv4_v7Y0zJwIv1UdoV05SLL3SWpT69LfQounsUOieFT=5DgeAcQ=QqzDvGyqARUSbeht1wf_j9Unb=yhhIf9aW0wI=QCEdCG3xVesZ_BAPbRnDBwIDd3f_=v34h60lSnmu=aWxWlnRPDmT=On6Kiqdz7T3NTNq7kj1rHlp46n_NR03Zl8PIKK-9JK4hy2_dGJJ_HeBsV_NAQhYQZ2XlHt5qcCdA8Vv9R1mPovHTp2I9hlt8h37KGq0NrkbT_ptZg1wUQvam_UvCamyZuLdBpn17tqgcV9ERH0gcSpa3zEKWwiiNFUj6qC1JFXDwmqQzOHbahd4xmVHBtiJYO5QgLW=Ohw=LC84ejIXesFk9QBaQfeQ0_wcaEdRl9=BJ82JjIKN8a9Jb_twD8JlsnloqstgITRyylSbfIy0_XtP-d23Wp5a-kLXhvyquQlgZKodBeiSj9HSSepYKqrD_FruDQZstPjvUvTdoavtvpKzBdn=eTx1edDzFoKkq_A=TXRX6V8lw8fSEpn6QfvBZCOgJuFG3r0TWrpRyPVizYYsLhF32saPQdx089tmf4uOL9o0AClxxatLkG8IVpax7HotQSG9rHA=GV1v1k9z8ZserPRrgYPo-Dn65SGax-68vhoocKBkaiVIVfRO_4BvU=ILK1uU3vOZfKcWPh9oNIy1T2t2OJfeQ1ccCR2=VTRR62B_XIFqDBN6SnO6R7N1qaoRVKmHbstCEnckYS1iZfwIUg69ejHRZB62DF8nkQ5W=8_enNK3KOrTwZFiamv-x89Yp3r3Izdy=fBXTOg5A5l1=hdgBLa8W=9PG9rbu4yfE0QLHU_LfJNdbiBxaoduzzAZIx-fi9BAr8w6s-uduRoBD-ERWsG5T=7GuPE_UZ1frDXrWvmhTQ6AoZxBc7gRO9Un3apjxH8SdDZLYnPZzy6BvJYZDxrlCdRi5W6Cc8SOGhAHHqJG-QY7toLTZeaSUT4JzbvynaHcLwAmooWFaxTerusVI9s5oRmkyAA_3qQWLy2hPnUiIRRaDPgHimhe8AVUegpFtfvcl-Z9NePAz6eS3zjAGc4kJy5x=EW17jHQoFpunJHlGa6F7OEfL7XHUc7X5jerbs0voYHWgE_uq6=xomY_i9ACCo2IxJCVdm=AWQtZ6lOr-7ureIUSUFFjx8SyJenjtJ1VSOHZLXFpTiC=jGb6yBa7WLmgEJDIlt1ymnBN2aQ-GtUCOZc4iBFwusv6kR5xtF4rUgikoxefoeTRtN_G7cRef--RoPfBACWXdmn9FbcL9qT21d2S7qVIZ9yTtZNTohRCn3WLW8XUGzSlCcp_uceWc-Pb6ZYUGtQfyxa5zKlvq9P65KpLshTRmXZGaeSg4lSmQD_6XhuEKN9y9GwcaQ=2uvFj5OVOEr_AxfvndxVd7rVi9vFgiUPp_pA1T8JZJyCOwK4SQil73SCybt_H2_x6UTrtYIVdQwxw1T=sRWG23ZDF6zsJl3XOUIN6fbsI-f_eOFUKQ_xdKmuRJQOf1ktQ_zmJrvzwOleQexI9lmLDyxBCnxUW2Kq-swXm8UsalfrgHhWYxq1waLfRS4V44Fk2FdfI=EIeATLqyL_Z_eCrZ3FjlNWQ2fgzpqhYjKyPidwTOo7JojrTTQ_UvPgbjm5FVB5czBoDuSEvHjz8OLCDZhFkxLPdOxiCZ79bItJKncLqqm3LQN28Z6hOC_4=WnOKi2hvKeIQD7twZq-S0zSrbHbsC=m_dv7aLNks7-R0kZxWBDttznEivp-gymmySgODnrXOrhU6CFBAQmQHikTvgw9daUNZYl5oWHr9kduels5w7tnyB10k5OOX_q3pUgtzmDfKDK3Iy9KeVDJamB4EZIGdA1q0=rRTkBHv82l3I7SnxNbdsorWR8Q09UTRolzTDia5vw_4-fl_p7p=AVQdwXyDZA0P5PBIfbhaut0Q9OWhE7If7Q9KlIuI8b5jIuiPOcAxS2U9LwwX2xJCaapS2=4FdgrTKuIsvEHTDZlvQe=W3x9ziV8_P1FRam0-9DA9fQz89v8k=3ha9GEUJDG1Jf0fX-uETE7LW=9QZuz4W7=qYOGpKxIPiPIX7gSbI3sCnEDni3ntl8qav5RIZDVsI1mG8ro61F=XqBDUJ-ZXGi8PO4lpqgVLh4y2xLmuwNIJICIfOAmm9edlWmCcY0rHfcj9o9Fq0ghUW8V08d0=GxauUTBKmn=slTkSL2YqtAXjXTUvpyt9T78ixck9N1H4GACmDemXTEjz0fUE7qO6cTobPbNgC3-cyjkVsG_DuFWET5A52tcPY4E6czF-82agrWs8ZNeDbRhILSBcSRczQVbyxQsv3gxrp=5O5xFO4=efkEVh2kn7_sYJSX0iK3attlkeAgqhrcbOWcniWx5FFA=aAw8AJwiRYcunROs-tRZ3CwNWJdsSxzJ_9bknthR4AHRKPNPqsEl-Y3ZzUNm8u-RtJ1rAdt_talpc4=tf0j5CwBrZHdPxh5zVI5T3Ee1ExbOuz4D=99djq7K1PTuvaZp1jpBErmrpIt6nLGdKGJRbpKoviX-ags97P9zcfQLE5im4Giq8GNW7D-9oETHf6GJ0il5flbGitql3B1qWFvF_f9I-82glIj8URkCLIJsIeOLfZ-EbVrnZgm1CD-OGwiy4azLi1VxJsWxKErQm09s4caivX9FKa1K5dBGmHbEJ_4ZgRvkq3qHzivENgtCXr6GjC4lD-lWp8BXHoo4cymPN4ZfkHABNqaI2loL0nivvaHsomrWED50a56xi4k9_NsdDx=p5-uUIBeXDke-Z3SC6_U8DrRN1Y3SE3SS9mDOxRuLbnZYPpR51Yx77OYHS68gUQ1ojxtdDKTX=wLJXW2O32bL5C4hFKD71ArnVZ18fEBzgo1La5LgpCtRFfcy3a2FwO4FERO_x-O=PfRYWjY2GYyASC-y8SWX9KFZo-I6jwU=AUO3tts_8R6wmbrhZ=nn83gyCldAuNDL2PLh-smEfQVtlQLmoZtBJzYY7glFUK0HXdHZzjSnY4PldcV==DYFHOc_=U7tEbGW=DQceB1nRX=VDv04AcJJlHrnF=YJ5t_JHP9dtKg79kj06h9esi4F_aKBzPS2tD3RWXKn_4v_FxWa3x1zxgGK6CmXYvr9jzCkKeD6YTdXeHrYXWAllfYtH0CnYIwpGcScVbZDBUoBW5urgLtUOHcbcr91izy6PsGBK92GBiI=I7mD42-Gc6KgvXod4YV5NOlBe1fP8zHPC5g0YV2KawzbQqA9JQptCBuQWl6dP=Jmsxs-4GTmc1Do_jSJHkg067BP7etAZK8vV31DlDb9-QCtG66B6zxDqNI_p90BO2IT1zBvHDCbD8CuIa-BWfWnlBq=sxJghlt1sb3EN1yd7VW_DOgUEA0uvseRC6VJ7-03xBN=ICkfgRaGG3PgxSs8BmihgimFcSzHrYGuplpy2Nz1r2Xg_Rw7nS_F2eCJo25E=WeaIfsweO1ZY5CWHqdpNvhYF0S=3TtW_vXKLcTF=a9h_Al7LwkCvR0HHnA9NgYOmcAx2e=RR2VgDQaKt-3XXFK_leF9NKkmhUGguELqGGhrKn7pygyfsoj2xwdZVgD_YEhekxK_B_xK0tQ=Q6uIh4vF1PCltOrCYFubDFhJzL4CvwFN9gvOIGAmcJGVrJBS7NFxJ04hTPlHu3spUH_w=23BAwyHbLP-2CRF394PwV8vuvvIvKRKFDFQHOrH9CbIp0GowELz9jBOFhuTQWmt-LWZ6wcHey2HfyzdbF23KTOrGlACXjKtSenSOV5sISHQLxTQ1Gux0i72GrGc0AsqSQBZUEmYANUxnZgqq0anxb1Ww9ZN_yyAHobc9xd6GGfU_83eexgYA6o4tj3HGnseasr_pYf-fLwoRK1iJS-=-ONh3JWvmrxKHhSst3roGw6nW79A2BPEI1CTz7Et=tPeKbmLgUzj56KnRTkZ-bSza7K6kBTz9Zq8mGw2BFjelcLn3DN3lKJfkAvAH-I6A7fVAFIm1iSdnElB1bx7AGsCyz8xP_P9QErWmBlLtqyDqJkPRnk9DNmmA61o7rAVRVdPI9VcNc_pZaqOJZ-euHAjDZQvvbGDP4_a-OOThkBU8G7OEj=O7oeu=orQu8u3z91tBgCk0EeHnvICv9SYIdqxjvhpuYXVYaNW4zEVpEx73uIpDZmSfHuifXViuo-3u99YPQFqYsDBlTOO_rr2Dp9PRlnyduFOxF=hspHnl9GLjs0h2rlyPK0s3Pd_u=houQHUGkZNhw-lHFVNTOWFbmNIAcVBYSw83442jbUY1DE68zCyt5-PTPe557tQ_w9EwU5Tr9KEUsq2vasUYtF9w9550oUuPV3Kb9w4857oULe41AzhlYlxzr97hTQXh0_dznS38IuAvcsJwn-mz79OrFuZ6AJiOy_EmFb4CsZZVZH2aPPNoOlQrpSXaKpvdD_jJ0OOvlL1kHv9eOBmP9CPyyTppnP79lc5=NPS7BGz=qlQpUvksFHjVGCfev40pXuoeF6Oqx4355lj=RLtwq_jaICbPJyE1XPVSXUiP6iYdP5=9cQ_tAoL1Ah4g2STLzfwJpQScJ793-cA1oiGiimnsGHtpBXTq=tqCBOql4WvJy22esItkfimU_umx4nImB1aEdAi-pOzNzwGI=RZaH6zp9nQoxhxPS=Lx56COCjtGpu996c_R0=D7VjnSocsuFqtU_-cxX1dse_JOEfBAJjKgO_d6pp09q6Emxt1zZBlb3ut1rYeDR9qJ8Vk5agHnTU_bDGBas=79plliWPG7oPeiZ88h9tbTE1-HwcKz-l3uVcI-rt0LHeO0VSu9xBlme5AlVHaQXOsqGNsHoSwP0FCTv9mTlRlPvg9nRE2A=BYw34qvR1yst6eukwiQJu_SUUqvZws4vEvBkeOZaCwC5H8CrdEaYFAAGUUQGG2UBNVHYFgtyfObEpC-IuxTCnmW5ViIaWqP8NH2gq=HAxUTk0nYl0IYNOEv5mZuS4XPIfEbyLyjVq6t9LeCj8XjqlDoLe-ReUPJQYVbWv23x5isNajU8b8LKJcpk=u5vXb1Q1XuQ1bZRRdjRemA9',
    'Xa4vrhYP3Q-z': 'q',
    'Xa4vrhYP3Q-d': 'ABaAhIDBCKGFgQGAAYIQgISigaIAwBGAzvpCzi_33wcxWwFwg-z0yAAAAABEJDeGCE5qulnvR2ZlyYZFs9VAyYw',
    'Xa4vrhYP3Q-c': 'AEAMdQSTAQAAVYr_4tGNEMrl5-9kYM_OUyUA9O294d8t-QYpfDFbAXCD7PTI',
    'Xa4vrhYP3Q-b': '-783e2c',
    'Xa4vrhYP3Q-f': 'A7OOhwSTAQAAAtMdu2BmICHL7Gb8ZvZlZFwzhwtRuWLBkpF9SUciAlKXp2M4AY5dRBGuct3FwH8AAEB3AAAAAA==',
    'query_caseNumber': 'B340000',
    'bot_check_1': 'Y',
    'bot_check_6': 'N',
    'submit': 'Search by Case Number',
    'bot_check_2': '',
}

response = requests.post(
    'https://appellatecases.courtinfo.ca.gov/search/searchResults.cfm',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

response.text







import requests
import random

url = "https://appellatecases.courtinfo.ca.gov/search/searchResults.cfm?dist=2&search=number"
headers = {
    "User-Agent": random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/90.0",
    ]),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://appellatecases.courtinfo.ca.gov",
    "Connection": "keep-alive",
}
response = requests.get(url, headers=headers)

"""





tentativas = 1


case = "B339494" #start case
case = "B339495" # with disposition
start_case = "B339494"#"B339507"
end_case = "B340000"
#end_case = "B339515"


start_number = int(start_case[1:])
end_number = int(end_case[1:])


case_numbers = [f"B{num:06d}" for num in range(start_number, end_number + 1)]

cases = ["B339494","B339495"]
cases = case_numbers
print(cases)
big_hash = {}

def generate_user_agent():
    browsers = [("Chrome", random.randint(70, 120)), ("Firefox", random.randint(60, 95))]
    os_types = ["Windows NT 10.0; Win64; x64", "Macintosh; Intel Mac OS X 10_15_7"]
    webkits = ["AppleWebKit/537.36 (KHTML, like Gecko)"]

    browser, browser_version = random.choice(browsers)
    os_type = random.choice(os_types)
    webkit = random.choice(webkits)
    safari_version = f"Safari/537.36" if browser == "Chrome" else ""

    return f"Mozilla/5.0 ({os_type}) {webkit} {browser}/{browser_version}.0 {safari_version}".strip()
"""
def generate_user_agent():
    browsers = [
        ("Chrome", random.randint(70, 120)),
        ("Firefox", random.randint(60, 95)),
        ("Safari", random.randint(10, 15)),
        ("Edge", random.randint(80, 95)),
    ]
    
    os_types = [
        "Windows NT 10.0; Win64; x64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "X11; Linux x86_64",
        "iPhone; CPU iPhone OS 14_6 like Mac OS X",
        "iPad; CPU OS 14_6 like Mac OS X",
        "Android 10; Mobile",
    ]
    
    webkits = [
        "AppleWebKit/537.36 (KHTML, like Gecko)",
        "AppleWebKit/605.1.15 (KHTML, like Gecko)",
    ]
    
    # Randomly choose browser, OS, and WebKit
    browser, browser_version = random.choice(browsers)
    os_type = random.choice(os_types)
    webkit = random.choice(webkits)

    if browser == "Chrome" or browser == "Edge":
        safari_version = f"Safari/537.36"
    elif browser == "Safari":
        safari_version = f"Safari/{random.randint(500, 605)}.1.15"
    else:
        safari_version = ""

    # Construct the User-Agent
    return f"Mozilla/5.0 ({os_type}) {webkit} {browser}/{browser_version}.0 {safari_version}".strip()

"""
"""
# Set path to your Chrome profile directory



"""


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48 Safari/537.36",
    # Add more User-Agents as needed
]


# Generate a list of 1000 unique User-Agents
user_agents = [generate_user_agent() for _ in range(1)]


user_agent = random.choice(user_agents)




chrome_profile_path = "user-data-dir=C:/Users/mateu/AppData/Local/Google/Chrome/User Data"



# Set Chrome options


user_arr = [
    "Default",
    "Profile 2",
    "Profile 3",
    "Profile 4",
    #"Profile 5",
    #"Profile 6",
    "Profile 7",
    "Profile 8",
    "Profile 9",
    ]
#driver = webdriver.Chrome(options=chrome_options)
def tudo(the_case):
    #breakpoint()

    chrome_options = Options()
    chrome_options.add_argument(chrome_profile_path)  # Use the existing Chrome profile
    selected_profile = random.choice(user_arr)
    chrome_options.add_argument(f"--profile-directory={selected_profile}")  # Specify the "Default" profile within the directory

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=chrome_options)
    
    
    
    #driver = uc.Chrome()
    
    
    #firefox_options = Options()
    #firefox_options.add_argument('--disable-blink-features=AutomationControlled')
    #firefox_options.set_preference("general.useragent.override", user_agent)
    #driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    #driver.set_window_size(1920, 1080)






    print(the_case)

    case = the_case
    search_terms = [
    "How to learn guitar",
    "Top 10 travel destinations",
    "Healthy smoothie recipes",
    "History of ancient Egypt",
    "Tips for better sleep",
    "Best movies of all time",
    "How to train a puppy",
    "Benefits of yoga",
    "Natural skincare tips",
    "Upcoming music festivals",
    "Cryptocurrency market trends",
    "Easy pasta recipes",
    "How to save money on groceries",
    "Popular video games 2024",
    "Home workout routines",
    "DIY home decor ideas",
    "How to improve memory",
    "Best science fiction books",
    "Photography tips for beginners",
    "Solar energy benefits",
    "How to start a blog",
    "Social media marketing tips",
    "Interior design trends",
    "Basic French phrases",
    "Latest in renewable energy",
    "Popular sports in Japan",
    "Best beaches in the world",
    "How to meditate effectively",
    "Top 10 museums in the world",
    "Benefits of mindfulness",
    "Introduction to stock trading",
    "History of the Roman Empire",
    "Famous artists of the Renaissance",
    "Must-read self-help books",
    "Virtual reality applications",
    "Budget travel tips",
    "How to play chess",
    "How to build a PC",
    "Best hiking trails",
    "Top universities in the USA",
    "How to improve public speaking",
    "Famous historical figures",
    "Introduction to blockchain",
    "Popular fitness trends",
    "How to make sushi at home",
    "Digital marketing strategies",
    "Basics of graphic design",
    "Ancient Greek mythology",
    "Understanding climate change",
    "Basics of gardening",
    "Top 10 programming languages",
    "Best smartphones 2024",
    "How to write a resume",
    "History of World War II",
    "How to create a YouTube channel",
    "Famous landmarks in Europe",
    "Benefits of drinking water",
    "Popular street foods",
    "Learning to play the piano",
    "How to set up a home office",
    "Difference between AI and ML",
    "How to make pizza at home",
    "Top books for entrepreneurs",
    "Benefits of a vegan diet",
    "Latest car models 2024",
    "How to practice mindfulness",
    "Gardening tips for beginners",
    "Mediterranean diet benefits",
    "Basic Spanish phrases",
    "What is the Internet of Things",
    "Learning to code for beginners",
    "Future of electric vehicles",
    "Introduction to psychology",
    "What is quantum mechanics",
    "Best exercises for abs",
    "How to organize a small space",
    "Popular pet breeds",
    "Essentials for camping",
    "Best online courses",
    "How to use Microsoft Excel",
    "Basics of photography",
    "Artificial intelligence in healthcare",
    "Healthy meal prep ideas",
    "How to write a novel",
    "Easy baking recipes",
    "Popular anime series",
    "Effective study techniques",
    "Top fashion trends",
    "Basics of investing",
    "Benefits of volunteering",
    "Understanding mental health",
    "Top 10 TV shows of all time",
    "Learning to play drums",
    "History of the Middle Ages",
    "How to start a podcast",
    "Understanding personal finance",
    "Tips for learning a new language",
    "Famous inventors in history",
    "Best places to see wildlife",
    "Difference between HTTP and HTTPS",
    "Popular tourist attractions",
    "How to improve time management",
    "Best recipes for kids",
    "What is machine learning",
    "Intro to astronomy",
    "Basics of cryptocurrency"
]
    
    def search_google():
        driver.get("https://www.google.com/")
        time.sleep(random.uniform(1, 3))  # Random delay
        search_box = driver.find_element(By.NAME, "q")
        search_term = random.choice(search_terms)
        search_box.send_keys(search_term + Keys.RETURN)
        print(f"Searched on Google: {search_term}")
        time.sleep(random.uniform(3, 5))  # Wait to simulate browsing

    # Define a function to perform a random search on Bing
    def search_bing():
        driver.get("https://www.bing.com/")
        time.sleep(random.uniform(1, 3))  # Random delay
        search_box = driver.find_element(By.NAME, "q")
        search_term = random.choice(search_terms)
        search_box.send_keys(search_term + Keys.RETURN)
        print(f"Searched on Bing: {search_term}")
        time.sleep(random.uniform(3, 5))  # Wait to simulate browsing

    # Loop to alternate searches between Google and Bing
    for _ in range(2):  # Number of searches to perform
        if random.choice([True, False]):
            search_google()
        else:
            search_bing()
    #driver.get(url)
    url = "https://appellatecases.courtinfo.ca.gov/search.cfm?dist=2&inputError=10"
    url = "https://appellatecases.courtinfo.ca.gov/search.cfm?dist=2"
    driver.get(url)
    #breakpoint()
    ####time.sleep(2)
    time.sleep(random.uniform(1, 3))
    
    
    case_number_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "query_caseNumber"))
    )
    
    
    
    
    #time.sleep(random.uniform(1, 3))
    
    case_number_input.send_keys(case)
    
    
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "caseNumberSubmit"))
    )
    
    #time.sleep(random.uniform(1, 3))
    submit_button.click()
    
    
    
    
    big_hash[case] = {}
    ######################error1#################
    try:
        
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{case}')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
    except:
        print("error1")
    
    ###############Parties and Attorneys###################
    
    big_hash[case]["Case Summary"] = None
    try:
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Case Summary')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
        ####time.sleep(random.uniform(5, 10))
        
        center_column = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "centerColumn"))
        )
        ####time.sleep(random.uniform(1, 3))
        center_column_html = center_column.get_attribute('innerHTML')
        
        
        soup = BeautifulSoup(center_column_html, 'html.parser')
        
        data_dict = {}
        rows = soup.select("div.clear10 ~ div.row")
        
        for row in rows:
            label = row.find("div", class_="col-xs-5 col-sm-3")
            value = row.find("div", class_="col-xs-7 col-sm-9")
            
            if label and value:
                label_text = label.get_text(strip=True)
                value_text = value.get_text(strip=True)
                data_dict[label_text] = value_text
        
        #print(data_dict)
        big_hash[case]["Case Summary"] = data_dict.copy()
    except:
        print(case,"no summary")
        
    
    #def get_parties_and_attorneys():

    
    ########Case Summary##########
    
    
    #def case_summary():
        

    
    
    #########Docket#########
    
    
    #def docket():
        
    big_hash[case]["Docket"] = None
    try:
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Docket')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
        ####time.sleep(random.uniform(5, 10))
        
        center_column = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "centerColumn"))
        )
        ####time.sleep(random.uniform(1, 3))
        center_column_html = center_column.get_attribute('innerHTML')
        soup = BeautifulSoup(center_column_html, 'html.parser')
        
        docket_table = soup.find("table", class_="table table-bordered")
        
        
        docket_entries = []
        
        
        for row in docket_table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) == 3:
                date = cells[0].get_text(strip=True)
                description = cells[1].get_text(strip=True)
                notes = cells[2].get_text(" ", strip=True) 
        
        
                docket_entries.append({
                    "Date": date,
                    "Description": description,
                    "Notes": notes
                })
                
                
        #print(docket_entries)
        big_hash[case]["Docket"] = docket_entries.copy()
    except:
        print(case,"no docket")
        
    #########Briefs#########
    
    
    
    #def briefs():
    big_hash[case]["Briefs"] = None
    try:
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Briefs')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
        ####time.sleep(random.uniform(5, 10))
        
        center_column = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "centerColumn"))
        )
        ####time.sleep(random.uniform(1, 3))
        center_column_html = center_column.get_attribute('innerHTML')
        soup = BeautifulSoup(center_column_html, 'html.parser')
        
        
        
        briefs_table = soup.find("table", class_="table table-bordered")
        
        
        briefs_entries = []
        
        
        for row in briefs_table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) == 5:
                brief = cells[0].get_text(strip=True)
                due_date = cells[1].get_text(strip=True)
                date_filed = cells[2].get_text(strip=True)
                party_and_attorney = cells[3].get_text(" ", strip=True) 
                notes = cells[4].get_text(strip=True)
        
                
                briefs_entries.append({
                    "Brief": brief,
                    "Due Date": due_date,
                    "Date Filed": date_filed,
                    "Party and Attorney": party_and_attorney,
                    "Notes": notes
                })
                
                
        #print(briefs_entries)    
        big_hash[case]["Briefs"] = briefs_entries.copy()
    except:
        print(case,"no Briefs")
    
    #########Scheduled Actions#########
    
    
    #def scheduled_actions():
    #breakpoint()
    big_hash[case]["Scheduled Actions"] = None
    try:
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Scheduled Actions')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
        
        ####time.sleep(random.uniform(5, 10))
        
        center_column = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "centerColumn"))
        )

        ####time.sleep(random.uniform(1, 3))
        center_column_html = center_column.get_attribute('innerHTML')
        soup = BeautifulSoup(center_column_html, 'html.parser')
        
        
        
        scheduled_actions_table = soup.find("table", class_="table table-bordered")
        
        
        scheduled_actions_entries = []
        
        
        for row in scheduled_actions_table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) == 3:
                description = cells[0].get_text(strip=True)
                due_date = cells[1].get_text(strip=True)
                notes = cells[2].get_text(strip=True)
                scheduled_actions_entries.append({
                    "Description": description,
                    "Due Date": due_date,
                    "Notes": notes
                })
                
                
        #print(scheduled_actions_table)
        big_hash[case]["Scheduled Actions"] = scheduled_actions_entries.copy()
    
    except:
        print(case, "no scheduled actions")
        
        
    
    #########Disposition#########
    #def disposition():
        
    try:
    
        big_hash[case]["Disposition"] = None
        
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Disposition')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
        ####time.sleep(random.uniform(1, 3))
        
        center_column = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "centerColumn"))
        )
        center_column_html = center_column.get_attribute('innerHTML')
        
        soup = BeautifulSoup(center_column_html, 'html.parser')
        
        
        
        disposition_entries = {}
        
    
        for row in soup.select("#DispositionList .row.flex-container"):
            label_div = row.find("div", class_="col-xs-5 col-sm-3 bold btn btn-default")
            value_div = row.find("div", class_="col-xs-7 col-sm-9 btn btn-default")
            
    
            if label_div and value_div:
                label = label_div.get_text(strip=True).replace(":", "")
                value = value_div.get_text(strip=True)
                
    
                disposition_entries[label] = value
                
                
        #print(disposition_entries)      
        big_hash[case]["Disposition"] = disposition_entries.copy()
    
    except:
        print(case,"no disposition_entries")
        
    big_hash[case]["Parties and Attorneys"] = None
    
    try:
    
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Parties and Attorneys')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
        ####time.sleep(random.uniform(5, 10))
        
        center_column = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "centerColumn"))
        )
        ####time.sleep(random.uniform(1, 3))
        center_column_html = center_column.get_attribute('innerHTML')
        soup = BeautifulSoup(center_column_html, 'html.parser')
        
        data = []
        for row in soup.find_all("tr"): 
            cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
            data.append(cols)
        
        
        df = pd.DataFrame(data)
        
        
        #print(df)
        
        
        big_hash[case]["Parties and Attorneys"] = df.to_dict(orient='records').copy()
    
    except:
        print(case,"no parties") 
    
    #########Trial Court#########
    
    #def trial_court():
    try:
    
        big_hash[case]["Trial Court"] = None
        
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Trial Court')]"))
        )
        #time.sleep(random.uniform(1, 3))
        button_to_click.click()
        ####time.sleep(random.uniform(1, 3))
        
        center_column = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "centerColumn"))
        )
        center_column_html = center_column.get_attribute('innerHTML')
        
        soup = BeautifulSoup(center_column_html, 'html.parser')
        
        
        trial_court_entries = []
        current_entry = {}
        
    
        for row in soup.select("div.clear10 ~ div.row"):
            label_div = row.find("div", class_="col-xs-5 col-sm-3 bold")
            value_div = row.find("div", class_="col-xs-7 col-sm-9")
            
            if label_div and value_div:
                label = label_div.get_text(strip=True).replace(":", "")
                value = value_div.get_text(strip=True)
        
                if label == "Trial Court Name" and current_entry:
                    trial_court_entries.append(current_entry)
                    current_entry = {}
        
    
                current_entry[label] = value
        
    
        if current_entry:
            trial_court_entries.append(current_entry)
                
                
        #print(trial_court_entries)
        big_hash[case]["Trial Court"] = trial_court_entries.copy()
    
    except:
        print(case,"no trial_court_entries")
    
    
    #breakpoint()
    driver.quit() 


"""

# Run in batches of 5
batch_size = 5
for i in range(0, len(cases), batch_size):
    # Select the next batch of cases
    batch = cases[i:i + batch_size]
    
    # Process the batch concurrently
    with concurrent.futures.ThreadPoolExecutor(batch_size) as executor:
        
        futures = [executor.submit(tudo, the_case) for the_case in batch]
        
        
        # Wait for all tasks in this batch to complete
        for future in concurrent.futures.as_completed(futures):
            pass  # Wait for each future in the batch to complete

    # After finishing each batch of 5 cases, execute the clicks
    print("Batch complete. Performing clicks...")
    pyautogui.click(x_center, y_center)
    #time.sleep(3)
    pyautogui.click(x_center, y_center)
    #time.sleep(6)

"""
for the_case in cases:
    try:
        tudo(the_case)
        print("Batch complete. Performing clicks...")
        time.sleep(3)
        #pyautogui.click(x_center, y_center)
        ####time.sleep(3)
        #pyautogui.click(x_center, y_center)
        ####time.sleep(6)
    except:
        print("fail")
        time.sleep(60)
        #time.sleep(637)


"""
for the_case in cases:
    tudo(the_case)
#    breakpoint()

with concurrent.futures.ThreadPoolExecutor(5) as executor:
    for the_case in cases:
        #time.sleep(13)
        executor.submit(tudo, the_case)

breakpoint()

    pyautogui.click(x_center, y_center)
    #time.sleep(3)
    pyautogui.click(x_center, y_center)
    #time.sleep(6)
        
"""   
""" 
sections = [
    get_parties_and_attorneys,
    case_summary,
    docket,
    briefs,
    scheduled_actions,
    disposition,
    trial_court,
]

# Shuffle the list to randomize the execution order
random.shuffle(sections)

# Execute each function in the randomized order
for section in sections:
    print(case,section)
    section()  # Call the function
""" 
        
        
        
        
        
        
        
        
import csv
        
        
def write_parties_and_attorneys(data, filename="parties_and_attorneys.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Case Number", "Party", "Attorney"])
        for case_number, case_data in data.items():
            if "Parties and Attorneys" in case_data and case_data["Parties and Attorneys"]:
                parties = case_data["Parties and Attorneys"]
                for party in parties[1:]:  # Only proceed if there are entries after the first item
                    writer.writerow([case_number, party.get(0, ""), party.get(1, "")])



def write_case_summary(data, filename="case_summary.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Case Number", "Trial Court Case", "Court of Appeal Case", "Division", "Case Caption", "Case Type", "Filing Date", "Completion Date", "Oral Argument Date/Time"])
        for case_number, case_data in data.items():
            if "Case Summary" in case_data and case_data["Case Summary"]:
                summary = case_data["Case Summary"]
                writer.writerow([
                    case_number,
                    summary.get("Trial Court Case:", ""),
                    summary.get("Court of Appeal Case:", ""),
                    summary.get("Division:", ""),
                    summary.get("Case Caption:", ""),
                    summary.get("Case Type:", ""),
                    summary.get("Filing Date:", ""),
                    summary.get("Completion Date:", ""),
                    summary.get("Oral Argument Date/Time:", "")
                ])




def write_docket(data, filename="docket.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Case Number", "Date", "Description", "Notes"])
        for case_number, case_data in data.items():
            if "Docket" in case_data and case_data["Docket"]:
                for docket in case_data["Docket"]:
                    writer.writerow([case_number, docket.get("Date", ""), docket.get("Description", ""), docket.get("Notes", "")])



def write_briefs(data, filename="briefs.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Case Number", "Brief", "Due Date", "Date Filed", "Party and Attorney", "Notes"])
        for case_number, case_data in data.items():
            if "Briefs" in case_data and case_data["Briefs"]:
                for brief in case_data["Briefs"]:
                    writer.writerow([
                        case_number,
                        brief.get("Brief", ""),
                        brief.get("Due Date", ""),
                        brief.get("Date Filed", ""),
                        brief.get("Party and Attorney", ""),
                        brief.get("Notes", "")
                    ])


def write_disposition(data, filename="disposition.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Case Number", "Description", "Date", "Disposition Type", "Publication Status", "Author", "Participants", "Case Citation"])
        for case_number, case_data in data.items():
            if "Disposition" in case_data and case_data["Disposition"]:
                disposition = case_data["Disposition"]
                writer.writerow([
                    case_number,
                    disposition.get("Description", ""),
                    disposition.get("Date", ""),
                    disposition.get("Disposition Type", ""),
                    disposition.get("Publication Status", ""),
                    disposition.get("Author", ""),
                    disposition.get("Participants", ""),
                    disposition.get("Case Citation", "")
                ])


def write_trial_court(data, filename="trial_court.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Case Number", "Trial Court Name", "County", "Trial Court Case Number", "Trial Court Judge", "Trial Court Judgment Date"])
        for case_number, case_data in data.items():
            if "Trial Court" in case_data and case_data["Trial Court"]:
                for trial in case_data["Trial Court"]:
                    writer.writerow([
                        case_number,
                        trial.get("Trial Court Name", ""),
                        trial.get("County", ""),
                        trial.get("Trial Court Case Number", ""),
                        trial.get("Trial Court Judge", ""),
                        trial.get("Trial Court Judgment Date", "")
                    ])


#breakpoint()
write_parties_and_attorneys(big_hash)
write_case_summary(big_hash)
write_docket(big_hash)
write_briefs(big_hash)
write_disposition(big_hash)
write_trial_court(big_hash)