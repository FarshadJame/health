import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    test_results = pd.read_excel(open("data/test-results.xlsx", 'rb'))
    positive_results = test_results[test_results["جواب آزمایش"] == 'positive']

    personal_information = pd.read_excel(open("data/personal-information.xlsx", 'rb'))

    # Inner Join
    positive_results_information = pd.merge(positive_results, personal_information, left_on='کدملی شخص',
                                            right_on='کدملی')

    positive_results_group_by = positive_results_information.groupby('تاریخ آزمایش', as_index=False).agg({
        'کدملی': 'count',
    })
    # sort
    positive_results_group_by_sort = positive_results_group_by.sort_values(by='کدملی', ascending=False).rename(
        columns={'کدملی': 'تاریخ آزمایش', 'تاریخ آزمایش': 'تعداد افراد مبتلا'})

    positive_results_group_by_three_row = positive_results_group_by_sort.iloc[:3]
    # answer part one
    print(positive_results_group_by_three_row)

    # answer part two
    positive_results_group_by_sort_date = positive_results_group_by.sort_values(by='تاریخ آزمایش',
                                                                                ascending=True).rename(
        columns={'کدملی': 'تاریخ آزمایش', 'تاریخ آزمایش': 'تعداد افراد مبتلا'})
    print(positive_results_group_by_sort_date)

    positive_results_group_by_sort_date.plot(x='تعداد افراد مبتلا', y='تاریخ آزمایش', kind='line')
    plt.show()
