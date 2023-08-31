import pandas as pd

merchant_df = pd.read_csv("dataset/merchant.csv")

offers_df = pd.read_csv("dataset/OFFERS.csv")

trans_df = pd.read_csv("dataset/transactions.csv")

users_df = pd.read_csv("dataset/USER.csv")


chennai_ppl = users_df[users_df["user_hometown"] == "CHENNAI"]

chennaippl_trans = chennai_ppl.join(
    trans_df.set_index("USER_ID"), on="user_id", how="inner"
)

chennaippl_trans_1 = chennaippl_trans[
    ["user_id", "user_name", "user_age", "user_income", "MERCHANT_ID", "AMOUNT"]
]

chennaippl_merchants = chennaippl_trans.join(
    merchant_df.set_index("MERCHANT_ID"), on="MERCHANT_ID", how="inner"
)

chennaippl_merchants.to_csv("./result.csv")
