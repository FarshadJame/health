import pandas as pd

if __name__ == '__main__':
    test_results = pd.read_excel(open("data/test-results.xlsx", 'rb'))
    negative_results = test_results[test_results["جواب آزمایش"].str.contains("egetive")]

    travel_information = pd.read_excel(open("data/travel-information.xlsx", 'rb'))
    cities = ["منچستر", "لندن", "بیرمنگام"]
    travel_information_filter = travel_information[(((travel_information["مبدا"].isin(cities)) | (
        travel_information["مقصد"].isin(cities))) & (travel_information["تاریخ سفر"] > 20200921) &
                                                    (travel_information["ورود/خروج"] == "ورود"))]

    national_id = pd.read_excel(open("data/national-id.xlsx", 'rb'))

    # Inner Join
    travel_information_with_nationId = pd.merge(travel_information_filter, national_id, how='inner',
                                                on=["گذرنامه"])

    # Inner Join
    travel_information_with_personal = pd.merge(negative_results, travel_information_with_nationId,
                                                how='inner',
                                                left_on='کدملی شخص',
                                                right_on='کدملی')
    travel_information_with_personal_sort = travel_information_with_personal.sort_values(by='تاریخ سفر', ascending=True)
    # answer part one
    travel_information_with_column = travel_information_with_personal_sort[['کدملی', 'تاریخ سفر']]

    # answer part two
    travel_information_with_personal_groupBy = travel_information_with_personal.groupby('مقصد', as_index=False)
    print(travel_information_with_personal_groupBy.first()['مقصد'])
