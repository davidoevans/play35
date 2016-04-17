import pandas as pd
import datetime as dt


def melt_employment():
    """
    The original CSV downloaded from open.canada has dates as columns and needs to be reformated as rows for
    Tableau to use it.

    :return:
    """
    df = pd.read_csv('/Users/davidevans/Google Drive/data/open.canada/esdc/cops/Employment_emploi_2015_2024.csv', encoding='iso-8859-1')
    df = pd.melt(df, id_vars=['Code', 'Occupation_Name', 'Nom_de_la_profession'], var_name="Year", value_name="Value")
    df.Year = [dt.datetime.strftime(dt.datetime.strptime(x, "%Y"), "%y-%b-%d") for x in df.Year]
    df.to_csv('/Users/davidevans/Google Drive/data/open.canada/esdc/cops/prepped_Employment_emploi_2015_2024.csv')

def prep_sudent_loan_by_jurisdiction():
    """

    :return:
    """
    df = pd.read_csv('/Users/davidevans/Google Drive/data/open.canada/esdc/20140831-01-27dvhist-eng.csv')
    df['Loan Year'] = [dt.datetime.strftime(dt.datetime.strptime(x, "%Y"), "%y-%b-%d") for x in df['Loan Year']]