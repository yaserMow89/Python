### Ceasar Cipher had a weakness point, and that is the fact that letters in English (not
### only English, almost all human languages) are distributed in a predictable way, and 
### they follow a specific pattern, to be more precise: q is usually followed by u in 
### english, e appears more than any other letter in english, z is least repeated letter
### in english.
### having a considerably long text, which is encrypted using Ceasar Cipher, counting the
### frequency of appereance for each of the letters, would equip us with every mean neccessary
### to decrypt the cipher
### the following code gets a text from the user and gives the frequency of repetation for 
### each letter in that text



def cal_frequencies(text):
  ### calculates the frequency for each letter in the given text
    frequency_dict = {}
    for char in text:
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    return frequency_dict

 
def cal_percentage(dict,all):
  ### returns the frequency by percentage for each letter in the given text and total number of repeatation
    percentage_dict = {}
    for key, value in dict.items():
        percentage_dict[key] = int((value / all) * 100)
    return percentage_dict


def pure_alphabet(text):
  ### The text that is given by the user at least includes spaces, this function omit everything nonalphabetical
    new_text = ""
    for char in text:
        if char.isalpha():
            new_text += char.lower()
    return new_text
  
def total_chars(dict):
  ### gives the total amount of the chars in the given text
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
print(cal_percentage(freq_dict, total_chars))
