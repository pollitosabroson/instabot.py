#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.instabot import InstaBot
from src.unfollow_protocol import unfollow_protocol

# sys.path.append(os.path.join(sys.path[0], 'src'))


# TOTAL TAGS 30
bot = InstaBot(
    login="username",
    password="password",
    like_per_day=180,
    media_max_like=15,
    media_min_like=15,
    tag_list=[
        'Photograph', 'Photographer', 'Vsco', 'Vscocam', 'Photographers_tr',
        'Photographie', 'Landscape_captures', 'Photographers @TopLikeTags',
        'Photographysouls', 'All_shots', 'Portrait', 'Vscocamphotos',
        'Likesforlikes', 'Photographs', 'Beautiful', 'Photographylovers',
        'TopLikeTags', 'Nature', 'TLTer', 'Outdoorphotography', 'Foto',
        'TopLikeTagsPhotography', 'Pictureoftheday', 'Likesreturned',
        'Silhouette', 'Picoftheday', 'Likeforlike', 'Art', 'Contrast',
        'Landscape'
    ],
    max_like_for_one_tag=30,
    log_mod=0,
    proxy='',
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
)
while True:

    # print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    # print("## MODE 1 = MODIFIED MODE BY KEMONG")
    # print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    # print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    # print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    # print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    # print("You choose mode : %i" %(mode))
    # print("CTRL + C to cancel this operation or wait 30 seconds to start")
    # time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            # unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 0:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                # follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
