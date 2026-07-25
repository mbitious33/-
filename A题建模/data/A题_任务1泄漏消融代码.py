# A题任务1泄漏消融实验
# 依赖：pandas numpy scikit-learn catboost
# 六组方案：
# A 保留全部时间信息
# B 删除Wake_Up_Time
# C 删除Wake_Up_Time与Sleep_Time
# D 删除Wake_Up_Time与Sleep_Duration_Hours
# E 删除Wake_Up_Time、Sleep_Time、Sleep_Duration_Hours
# F 在E基础上继续删除睡眠质量、夜醒、周末睡眠差、小睡、睡前屏幕和睡眠障碍风险
#
# 验证方式：StratifiedKFold(n_splits=3, shuffle=True, random_state=2026)
# 模型：CatBoostClassifier(iterations=35, depth=5, learning_rate=0.18)
