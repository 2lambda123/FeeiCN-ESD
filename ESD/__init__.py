#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ESD
    ~~~

    Implements enumeration sub domains

    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/FeeiCN/ESD
    :license:   GPL, see LICENSE for more details.
    :copyright: Copyright (c) 2018 Feei. All rights reserved
"""
import sys

if __name__ == '__main__':
    # Python版本判断，因采用了Asyncio等特性，仅在Python3及以上可运行。
    if sys.version_info.major < 3:
        print('Python 3 or higher is required for ESD, upgrade your python please!')
        sys.exit(1)
    # 提前引入Python3代码会导致报错
    import EnumSubDomain

    EnumSubDomain.main()
