from bs4 import BeautifulSoup as bs
import pandas as pd


def response_process(content):
    output = {}
    bs_content = bs(content, "lxml")
    columns_list = [tag.name for tag in bs_content.find("ns3:standardizegloballocationoutputrow").find_all()]
    for ele in columns_list:
        output[ele.replace("ns3:", "")] = bs_content.find(ele).text
    return pd.Series(output)
