import wbgapi as wb
import pandas as pd
pd.set_option('display.max_columns', None)


def grab_year_based_data(dictionary, economy, time):
    '''
    Allows user to grab any series data from a given year
    :param dictionary:
    :param economy:
    :param time:
    :return:
    '''

    df = pd.DataFrame(columns=['description', 'period'])

    for key, value in dictionary.items():
        a = wb.data.DataFrame(series=key, economy=economy, time=time,
                              labels=True).reset_index()
        a = pd.melt(a, id_vars=['Country', 'economy'])

        df = pd.concat([df, a])

        # adding description to relevant cells now
        if df['description'].isnull:
            df['description'].fillna(value=value, inplace=True)
        else:
            continue

        # adding time period to relevant cells
        if df['period'].isnull:
            df['period'].fillna(value=time, inplace=True)
        else:
            continue

    df = df.rename(columns={"variable": "seriesId", "Country": "country"})
    # df['period'] = pd.to_datetime(df['period'], format='%Y')
    return df


def grab_multi_year_data(dictionary, start, end):
    '''
    allows user to grab multi year data
    :param dictionary:
    :param economy:
    :param start:
    :param end:
    :return:
    '''

    df = pd.DataFrame(columns=['description', 'seriesId'])

    for key, value in dictionary.items():
        a = wb.data.DataFrame(series=key,
                              time=range(start, (end + 1)),
                              labels=True).reset_index()
        a = pd.melt(a, id_vars=['economy', 'Country'])
        df = pd.concat([df, a])

        # adding description to relevant cells now
        if df['description'].isnull:
            df['description'].fillna(value=value, inplace=True)
        else:
            continue

        # adding series id as well because it is not included
        if df['seriesId'].isnull:
            df['seriesId'].fillna(value=key, inplace=True)
        else:
            continue

    df = df.rename(columns={"variable": "period", "Country": "country"})
    df['year'] = df['period'].str[2:]
    # df['period'] = pd.to_datetime(df['period'], format='%Y')
    return df


def combine_year_based_dfs(dfs):
    combined_df = pd.concat(dfs, axis=0, ignore_index=True)
    return combined_df
