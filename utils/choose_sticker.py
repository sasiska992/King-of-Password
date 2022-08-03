import random

googling_sticers = ["CAACAgIAAxkBAAIceWLC9vsuPktu62e6NojLUPDo4zkxAAJFAANZu_wl-9SkNOET-OspBA",
                    "CAACAgIAAxkBAAIcfGLC9vvZ4hNjSQnrzZE-UkBaHy54AAI4CwACTuSZSzKxR9LZT4zQKQQ",
                    "CAACAgIAAxkBAAIchmLC9yBdcnkxuPGHeWsIP5UP7HgXAAIgCQACGELuCOGKIKihOgrZKQQ",
                    "CAACAgIAAxkBAAIciWLC9yACplW_UT799heYVdyBXy0MAAIFAQAC9wLID9HldLdGJaShKQQ",
                    "CAACAgIAAxkBAAIcj2LC9yiWOgeNMO26ogm1n96zzljKAAKIGQACOpsQSyCDo8nnQMhrKQQ",
                    "CAACAgIAAxkBAAIclGLC9y0SQTe2gR9jNLJPZkqJRsR6AAKBAQACK15TC14KbD5sAAF4tCkE"
                    ]

knowing_stickers = ["CAACAgIAAxkBAAINemKuMWCrgro0JxWkjEDt-ZB0Lp3_AAJdAAPBnGAMc2BW3CfA5CokBA",
                    "CAACAgIAAxkBAAINe2KuMXeak4PnUkDA-WtqCDtOu2SPAAKQEQAChQZISx_NBb30yYWxJAQ",
                    "CAACAgIAAxkBAAINfGKuMZiNjHfOBtTIYQj7Pg0KvN_VAAKEDQAChNn4Sn8hSkm3QU8kJAQ",
                    "CAACAgIAAxkBAAINfWKuMZreR1TvWXxETvZsP0UduYeOAAK5DgACRtvASWgWBBOZ_cFuJAQ",
                    "CAACAgQAAxkBAAINfmKuMasll33Rq80X7hbXg5NrqUqIAAJbCAAClVchUMI8hcAn5dmdJAQ",
                    "CAACAgQAAxkBAAINf2KuMbKXC3XWzgGjCf2JYjK0XjiwAAKjCQACLmg5UKEbrbUccROgJAQ",
                    "CAACAgQAAxkBAAINgGKuMbknv-PDL96uWatxBga6KToVAALpCQACWYNoUmOriFnrBvCHJAQ",
                    "CAACAgIAAxkBAAINo2KuM4wK_niycfYRspMD818TkhabAALDEwACbegQSoZjwH3h3Lo0JAQ",
                    "CAACAgIAAxkBAAINpGKuM49RQ35n39oKVgYhptKxz7B2AALgAAOWn4wOUr49XZjLh8ckBA",
                    "CAACAgIAAxkBAAINpWKuM5nvKzVu_BsL-KJvKBrO7YifAAJjDgACd3nQSmfew2Z0ISbTJAQ",
                    "CAACAgIAAxkBAAINp2KuM7KV_Dl1otff5RpaYD5BAAGw7AACmQgAAkVRkw67fI_Mkpi9RSQE",
                    "CAACAgIAAxkBAAINqGKuM9AwgobX4K7kgxKNk5D_lmiTAAIoAANuu201IIhCu4vn68okBA",
                    "CAACAgIAAxkBAAINqWKuM92udZF7mNN6WhnQr1jlT5A1AAI7AwACbbBCAwOCj__lcU91JAQ",
                    "CAACAgIAAxkBAAINqmKuNAKE5U8OUJFydux9CQUFCGa4AAJLAANdBYIW1IuJ2vd7zcAkBA",
                    "CAACAgIAAxkBAAINq2KuNA_ieXXnXBkifvbFFcQl0JYQAAIfCQACRVGTDu_8zwqMfKjaJAQ",
                    "CAACAgIAAxkBAAIclmLC97nHH5Un6MkF6Q3p9NwahMPSAAJaAwACusCVBcTyNiBsOifFKQQ",
                    "CAACAgIAAxkBAAIcmWLC97kqYHXb-YG3pFsIJfyq_w83AAJ4AgACVp29Cvy6CLWRfRwMKQQ",
                    "CAACAgIAAxkBAAIcnGLC97mkw-Lsbo9TgBEfDkcr0s0ZAAImCQACGELuCKOr8kYx-KOOKQQ",
                    "CAACAgIAAxkBAAIcn2LC97k3FGHb7TOtvGn3IVkvR3JhAAK3AAP3AsgPkPG2BzshSB0pBA",
                    "CAACAgEAAxkBAAIcq2LC-BLeDfwsLypjB1KRSqKcWi4mAAIeAQACOA6CEUZYaNdphl79KQQ",
                    "CAACAgIAAxkBAAIcr2LC-BLK9bk9SN-O8UjB7zUgbIIuAAI9AANSiZEj56KM1HtGgRApBA",
                    "CAACAgIAAxkBAAIctGLC-CdTDLEEZbQjaUsdi8sIWVpYAAImCQACGELuCKOr8kYx-KOOKQQ",
                    "CAACAgIAAxkBAAIcuGLC-Ce_d_o6ncIV0obg9D68CIh4AAJtAAPkoM4HiFOGcq2yHRspBA",
                    "CAACAgIAAxkBAAIcu2LC-EPoKkLUUvrzCe8V3Dg3nvKbAAI9AANSiZEj56KM1HtGgRApBA",
                    "CAACAgIAAxkBAAIcv2LC-E9MGWsaa1feTv8iy8kuCghkAAK3AAP3AsgPkPG2BzshSB0pBA",
                    "CAACAgIAAxkBAAIcwWLC-FTa-8Z-WNU1w5xQXiV0PJ0HAAJtAAPkoM4HiFOGcq2yHRspBA"]

happy_stickers = ["CAACAgIAAxkBAAIM0GLUGwg9sTQ-7XUy2jTNiYJeGX_MAAKtGAACMGzBSTAFoKYyH4doKQQ",
                  "CAACAgIAAxkBAAIM02LUGxH0qAhqlwAB9gn1MgrgRTi9AQACQAEAAlKJkSM2vVjaS6yQ6Ck",
                  "CAACAgIAAxkBAAIM1mLUGxYTyyIONHKoG3jTiOVtH7oPAALKAAP3AsgPBCT_iBPotMMpBA",
                  "CAACAgIAAxkBAAIM2WLUGxoj9M4skiQn0v4DCLENGaFHAAKvAAP3AsgPrAmN36vGr4kpBA",
                  "CAACAgEAAxkBAAIM3GLUGx_wgSv4yv01rGxLCRvOD6OVAAL_AAM4DoIRy3vWd2ul3nUpBA",
                  "CAACAgIAAxkBAAIM32LUGyI43cc3NoK_qEO3rBMAAV_ZMAACswsAAipQUUoso7YJ7GnT1ikE",
                  "CAACAgIAAxkBAAIM4mLUGyfjhOxozhmtu59dqdbPdKXHAAJiAAN4qOYPiW9skvfBcb8pBA",
                  "CAACAgIAAxkBAAIM5WLUGzPxwDVEB7sq97Dfq-Y8ll8TAAJ3BQACP5XMCmWM0yxKQdlOKQQ",
                  "CAACAgIAAxkBAAIM6GLUGzzerYGhUDHOxtNBq7Pjw-OHAAJMAQACMNSdEffeb183gzkcKQQ",
                  "CAACAgIAAxkBAAIpMmLUHkDmuO3DtR2phr0cVrUi8UXoAAJYAANZu_wlSUQ6ZogUUNEpBA",
                  "CAACAgIAAxkBAAIpM2LUHkRnLMeKmc9lmvdNGAQ-I717AAL8AAMw1J0RU6XxJu0oNegpBA",
                  "CAACAgIAAxkBAAIpNGLUHkn2yAaD1k0Gei-TZ8NX3nqIAAJUAQACIjeOBJ6cKg4hDmDNKQQ",
                  "CAACAgIAAxkBAAIpNWLUHk8q_Qza9OH6SVGGewAB93SbNAAC0QAD9wLID7DVFiL6IbHMKQQ",
                  "CAACAgIAAxkBAAIpNmLUHlSsaLO0_ULJ1zecy4xHH9-1AAIkAAOymJoOXfnDiNVs2SApBA",
                  "CAACAgIAAxkBAAIpN2LUHl7QvK32QGVPhkBwi3OGRyBpAAIrAAN4qOYPJV9pEP5R6jopBA",
                  "CAACAgIAAxkBAAIpOGLUHmNvHmQabl7WKFygypRTx1LTAAIdAAOvxlEaXI764QrPb7wpBA",
                  "CAACAgIAAxkBAAIpOWLUHmwWSb8IQtIKuysrHPqOYL18AAJfAAPBnGAMLpRna9tNe9QpBA",
                  "CAACAgIAAxkBAAIpOmLUHnJATwiYsns5ApIXbAYdCeuWAAJwDAACDzUgS0IGOplsVK2mKQQ",
                  "CAACAgIAAxkBAAIpO2LUHoHD04d9ctPD7gZfTSrSttK8AAIaAQACUomRI8ZiamhhiWL9KQQ"
                  ]

banned_stickers = ["CAACAgIAAxkBAAIOK2KuNrRcogltDYTKb8-3Ct1TJ-_mAAKmAANTDGcaMR7rtQ6BSEskBA",
                   "CAACAgIAAxkBAAIOLGKuNvy11RSWUcigHWHjSkK-yY7ZAAKAFAACogc5SKU0NNbvUtQzJAQ",
                   "AAMCAgADGQEAAgzNYtQKW8NZfCEdlXjT8olWZ4wY_14AAg0VAAK4VBhLunJqQigYZIMBAAdtAAMpBA",
                   "CAACAgIAAxkBAAIwgmLapRtzcewrTYf-Xwv6oS6WL5CrAAKjAANTDGcaYokPkWdJV4YpBA"]


async def get_sticker(dp, message):
    sticker_set_names = ["catsforksushamylove_by_fStikBot",
                         "NilTheesAyahs_by_fStikBot",
                         "cj25cutecat25cj_by_fStikBot",
                         "pussis",
                         "Apqqqpp",
                         "cj25cutecat25cj_by_fStikBot"]
    sticker_set_name = random.choice(sticker_set_names)
    sticker_set = dict(await dp.bot.get_sticker_set(name=sticker_set_name))
    sticker_name = sticker_set.get("stickers")
    sticker_pack = []
    for i in sticker_name:
        sticker_id = i.get("file_id")
        sticker_pack.append(sticker_id)
    sticker = random.choice(sticker_pack)
    if sticker in banned_stickers:
        await get_sticker(dp, message)
    else:
        return sticker
