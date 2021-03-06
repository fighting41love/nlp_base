# -*- coding: utf-8 -*-
"""
CONFIG
------
对配置的封装
"""
config_instance = None


class Config:

    def __init__(self):
        self.config_dict = {
            'train': {
                # 自定义词典
                'user_dict_path': 'data/comment_userdict.txt.gz',

                # 原始语料：标签与句子用空格分隔开
                # 标签格式: 三分类-(1,2,3)
                'corpus_path': 'data/comment.txt',

                # 分割后语料:用空格分割开的词组,第一个为标签
                # 标签格式:三分类-(__label__1, __label__2, __label__3)
                'seg_corpus_path': 'data/comment_seg.txt',

                # 增加语料预采样的地址
                'sample_corpus_path': 'data/comment_sample.txt',

                # 是否进行预采样
                'sample': '',

                # 词典地址
                'vocabs_path': 'data/vocabs.txt',

                # 模型地址
                'model_path': 'data/model',
            },
            'test': {
                # 测试原始语料
                'test_corpus_path': 'data/comment_test.txt',

                # 测试分割语料
                'test_seg_corpus_path': 'data/comment_test_seg.txt',
            },
            'model': {
                'lr': 0.01,
                'lr_update_rate': 100,
                'dim': 300,
                'ws': 5,
                'epoch': 10,
                'word_ngrams': 3,
                'loss': 'hs',
                'bucket': 2000000,
                'thread': 4,
                'silent': 1,
            }
        }

    def get(self, section_name, arg_name):
        return self.config_dict[section_name][arg_name]


def get_config():
    global config_instance
    if not config_instance:
        config_instance = Config()
    return config_instance
