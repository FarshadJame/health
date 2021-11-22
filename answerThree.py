import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    test_results = pd.read_excel(open("data/test-results.xlsx", 'rb'))
    positive_results = test_results[
        ((test_results["جواب آزمایش"] == "positive") & (test_results['تاریخ آزمایش'] > 20210119) & (
                test_results['تاریخ آزمایش'] < 20210219))]

    states = pd.read_excel(open("data/states.xlsx", 'rb'))

    # Inner Join
    positive_results_with_state = pd.merge(positive_results, states, left_on='شهر آزمایش',
                                           right_on='استان')
    positive_results_with_state_group_by = positive_results_with_state.groupby('استان', as_index=False).agg({
        'کدملی شخص': 'count',
    }).rename(
        columns={'کدملی شخص': 'تعداد افراد مبتلا'})

    # answer part one
    print(positive_results_with_state_group_by.sort_values(by='تعداد افراد مبتلا', ascending=False).iloc[:3])

    # answer part two
    print(positive_results_with_state_group_by.sort_values(by='تعداد افراد مبتلا', ascending=True).iloc[:3])

    df = positive_results_with_state_group_by.sort_values(by='تعداد افراد مبتلا', ascending=False)
    df.plot(x='استان', y='تعداد افراد مبتلا', kind='bar')
    plt.show()
