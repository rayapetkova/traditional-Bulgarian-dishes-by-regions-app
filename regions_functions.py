from base_region_class_structure import BaseRegion
from helpers import clean_widgets_from_frame


def north_western(main_window):
    curr_frame = BaseRegion(main_window,
                            'North Western Region', 'north_western_region',
                            'lyutika', 'Lyutika',
                            'Traditional vegetable mixture - \nsalad or chunky relish, popular in \nthe '
                            'northern part of Bulgaria.\nIt is consumed in the summer.',
                            228, 320, 200, 495,

                            'turlashka_banitsa', 'Turlashka Banitsa',
                            'One of the most iconic dishes of the \nregion.nThe dough '
                            'is divided and \nrolled out into squares to be baked \non '
                            'the top of a wood-burning stove.',
                            534, 320, 573, 495,

                            'kosachko_kiselo', 'Kosachko Kiselo',
                            'A cold and refreshing soup that is \ntraditionally prepared '
                            'only \nin Torlashko and only in summer.',
                            928, 320, 962, 495)

    return curr_frame


def north_central(main_window):
    curr_frame = BaseRegion(main_window,
                            'North Central Region', 'north_central_region',
                            'makarina', 'Makarina',
                            'A traditional Bulgarian banitsa \nthat consists of several layers of \nfilo dough '
                            'and filling. It is \nconsumed during holidays.',
                            205, 320, 190, 495,

                            'oven_baked_mish_mash', 'Oven-Baked Mish-Mash',
                            'A typical dish of the region, which \ndiffers from the usual mish-mash '
                            '\nbecause it contains cheese \nand is not cooked in a pan.',
                            498, 320, 573, 495,

                            'piltseta', 'Piltseta',
                            'A popular dish that can be \nserved with yogurt at various \n'
                            'holidays and family gatherings. \nThey can be consumed hot or cold.',
                            990, 320, 962, 495)

    return curr_frame


def north_eastern(main_window):
    curr_frame = BaseRegion(main_window,
                            'North Eastern Region', 'north_eastern_region',
                            'plateki', 'Plateki',
                            'Thin, flat breads that are known for \ntheir crispy texture and taste. \n'
                            'They are made from rolled dough and \nare usually cooked on a hot griddle.',
                            215, 320, 190, 495,

                            'zelnik', 'Zelnik',
                            'A classic green banitsa with cheese \nand eggs, in which boiled or fried \n'
                            'saturated fresh cabbage is \nadded. Leeks can also be added.',
                            610, 320, 573, 495,

                            'fish_soup', 'Fish Soup',
                            "Traditional dish that showcases \nthe region's proximity to the \n"
                            "Black Sea. It is commonly served \n"
                            "during the summer months.",
                            975, 320, 962, 495)

    return curr_frame


def south_western(main_window):
    curr_frame = BaseRegion(main_window,
                            'South Western Region', 'south_western_region',
                            'banska_kapama', 'Banska Kapama',
                            'A typical dish from Bansko, \nwhere the tradition is still \npreserved and is shared '
                            'at the \ntable by many Bulgarians.',
                            165, 320, 190, 495,

                            'tseluvarchi', 'Tseluvarchi',
                            'A lean dish from traditional cuisine \nin Bansko. On Christmas Eve, '
                            '\nan odd number of lean dishes \nare put on the table, and \nthis can be one of them.',
                            580, 320, 573, 495,

                            'chomlek', 'Chomlek',
                            'This popular dish is a delicacy \nfrom the Pirin region. It is '
                            'served \nhot and is usually accompanied \nby fried potatoes or bread.',
                            975, 320, 962, 495)

    return curr_frame
