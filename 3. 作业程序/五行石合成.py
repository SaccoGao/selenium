# Demo题目：合成五行石
# 条件 消耗：金、钻石、体力
# 够买1级五行石需要消耗：金和钻石
# 1级五行石合成3级五行石需要消耗：金、体力、1级五行石
# 3级五行石合成4级五行石需要消耗：金、体力、1级五行石、一定概率
# 4级五行石合成6级五行石需要消耗：金、体力、4级五行石

# 购买1级石头
l1_value_gold = 0.75  # 1颗1级石头消耗0.75金
l1_value_diamond = 8  # 1颗1级石头同时消耗8个钻石

# 1级石头合成3级石头
l1_to_l3 = 12  # 需要消耗1颗1级石头 和 12颗1级石头
l1_to_l3_gold = 0.39  # 同时需要0.39金
l1_to_l3_vit = 10  # 同时需要10点体力

# 3级石头合成4级石头
l3_to_l4 = 16  # 需要消耗1颗3级石头 和 16颗1级石头
l3_to_l4_gold = 0.897  # 同时需要0.897金
l3_to_l4_vit = 10  # 同时需要10点体力
l3_to_l4_rate = 0.4878  # 成功概率 0.4878 失败则不扣除体力，只消耗 金币和16个1级石头

# 4级石头合成6级石头
l4_to_l6 = 12  # 需要消耗1颗4级石头 和 12颗4级石头
l4_to_l6_gold = 19.75  # 同时需要19.75金
l4_to_l6_vit = 10  # 同时需要10点体力

# 已知1颗6级石头市场售价是750金,请问是自己合成划算还是直接购买划算
# 其他数据：
# 1颗钻石（diamond） = 0.05金
# 1点体力（vit） = 1金

import random

# 购买1颗1级石头需要消耗的金
count_l1_gold = l1_value_gold + l1_value_diamond * 0.05
print("合成1颗1级石头需要：" + str(count_l1_gold) +"金")

# 合成1颗3级石头所需金
def count_l3():
    count_l3_gold = (l1_to_l3_gold + l1_to_l3_vit + (l1_to_l3 + 1) * count_l1_gold)
    count_l3_gold_str = str(count_l3_gold)
    return count_l3_gold

count_l3_gold = count_l3()
print("合成1颗3级石头需要：" + str(count_l3_gold) +"金")

# 合成1颗4级石头所需金
def count_l4():
    gl = format(random.random(),'.4f')
    gl = float(gl)
    if gl <= 0.4878:
        count_l4_gold_T = (count_l3_gold + count_l1_gold * 16 + l3_to_l4_gold + l3_to_l4_vit)
        return count_l4_gold_T,gl
    elif gl > 0.4878:
        count_l4_gold_F = (count_l1_gold * 16 + l3_to_l4_gold)
        return count_l4_gold_F,gl

count_l4()
count_l4_gold = count_l4()
print("合成1颗4级石头，成功需要：" + str(count_l4_gold) +"金")
# 合成1颗6级所需金
l6_num = 0
l4_num = 0
count_num = 0
count_num_T = 0
count_num_F = 0
count_l6_gold = 0

while l4_num < 13:
    count_l4()
    count_l4_gold = count_l4()
    if count_l4_gold[1] <= 0.4878:
        l4_num += 1
        count_l6_gold += count_l4_gold[0]
        count_num += 1
        count_num_T += 1
    elif count_l4_gold[1] > 0.4878:
        count_l6_gold += count_l4_gold[0]
        count_num += 1
        count_num_F += 1

count_l6_gold = count_l6_gold + l4_to_l6_gold + l4_to_l6_vit

print("本次合成次数为：" + str(count_num) + "次\n其中")
print("成功次数为：" + str(count_num_T) + "次")
print("失败次数为：" + str(count_num_F) + "次")
print("总计消耗：" + str(format(count_l6_gold,".0f")) + "金")

# 计算机结果
# 1颗1级：1.15金
# 1颗3级：25.34金
# 合成4级，成功：54.637金
# 合成4级，失败：19.297金