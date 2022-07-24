
def cal_frequencies(text):
    frequency_dict = {}
    for char in text:
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    
    return frequency_dict

def cal_percentage(dict,all):
    percentage_dict = {}
    for key, value in dict.items():
        percentage_dict[key] = ((value / all) * 100)

    return percentage_dict


def pure_alphabet(text):
    new_text = ""
    for char in text:
        if char.isalpha():
            new_text += char.lower()
    
    return new_text

def shortened_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        str_val = str(value)
        new_dict[key] = str_val[:4]
    return new_dict

# def sorted_dict(dict):
#     new_sorted_dict = {}
#     counter = len(dict)
#     while counter >= 0:
#         current_key = dict[0]
#         for key,value in dict.items():
#             pass       

def total_chars(dict):
    total = 0
    for key, value in dict.items():
        total += value
    return total

test_text = "LOJUM YLJME PDYVJ QXTDV SVJNL DMTJZ WMJGG YSNDL UYLEO SKDVC \
GEPJS MDIPD NEJSK DNJTJ LSKDL OSVDV DNGYN VSGLL OSCIO LGOYG \
ESNEP CGYSN GUJMJ DGYNK DPPYX PJDGG SVDNT WMSWS GYLYS NGSKJ \
CEPYQ GSGLD MLPYN IUSCP QOYGM JGCPL GDWWJ DMLSL OJCNY NYLYD \
LJQLO DLCNL YPLOJ TPJDM NJQLO JWMSE JGGJG XTUOY EOOJO DQDMM \
YBJQD LLOJV LOJTV YIOLU JPPES NGYQJ MOYVD GDNJE MSVDN EJM" 

pured_alphabet = pure_alphabet(test_text)
freq_dict = cal_frequencies(pured_alphabet)
total_chars = total_chars(freq_dict)
percentage_calculated_dict = cal_percentage(freq_dict, total_chars)
final_shortened_dict = shortened_dict(percentage_calculated_dict)
print(final_shortened_dict)
