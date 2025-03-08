import random

# 定义颜色列表
COLORS = ['红', '橙', '黄', '绿', '蓝', '靛', '紫']

def generate_secret_code():
    """生成一个由4种不同颜色组成的随机密码"""
    return random.sample(COLORS, 4)

def get_feedback(secret_code, guess, mode='simple'):
    """根据玩家的猜测和密码，给出反馈"""
    feedback = []
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            feedback.append('绿')  # 颜色和位置都正确
        elif guess[i] in secret_code:
            feedback.append('白')  # 颜色正确但位置不对
        else:
            feedback.append('红')  # 颜色错误

    if mode == 'hard':
        random.shuffle(feedback)  # 困难模式下，反馈顺序随机
    return feedback

def display_feedback(guess, feedback, mode='simple'):
    """显示玩家的猜测和反馈"""
    if mode == 'simple':
        print("你的猜测:", guess)
        print("反馈:", feedback)  # 简单模式下，反馈顺序明确
    else:
        print("你的猜测:", guess)
        print("反馈:", feedback, "(顺序未知)")  # 困难模式下，反馈顺序随机

def introduce():
    """程序的自我介绍功能"""
    print("=" * 50)
    print("欢迎来到颜色解谜游戏！")
    print("=" * 50)
    print("游戏规则：")
    print("1. 系统会从以下颜色中随机选择4种不同的颜色组成密码：", COLORS)
    print("2. 你需要猜测这4种颜色的排列顺序。")
    print("3. 每次猜测后，系统会给出反馈：")
    print("   - 绿灯：颜色和位置都正确")
    print("   - 白灯：颜色正确但位置不对")
    print("   - 红灯：颜色错误")
    print("4. 你可以选择简单模式或困难模式：")
    print("   - 简单模式：反馈直接显示在猜测下方，顺序明确")
    print("   - 困难模式：反馈顺序随机，你需要自己判断")
    print("5. 你可以自定义猜测次数（直接按回车表示无限次数）。")
    print("6. 如果你想提前结束游戏，请输入“答案”或“退出”。")
    print("=" * 50)
    print("开发者：XZD")
    print("版本：1.2")
    print("=" * 50)
    print()

def main():
    introduce()  # 显示自我介绍

    mode = input("请选择模式（简单/困难）：").strip().lower()
    while mode not in ['简单', '困难']:
        mode = input("请输入'简单'或'困难'：").strip().lower()

    # 玩家决定猜测次数（留空表示无限次数）
    while True:
        max_attempts_input = input("请输入你想尝试的次数（直接按回车表示无限次数）：").strip()
        if max_attempts_input == "":
            max_attempts = float('inf')  # 无限次数
            break
        try:
            max_attempts = int(max_attempts_input)
            if max_attempts <= 0:
                print("猜测次数必须大于0，请重新输入。")
            else:
                break
        except ValueError:
            print("请输入一个有效的数字。")

    secret_code = generate_secret_code()
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        print(f"\n第 {attempts} 次尝试：")
        guess = input("请输入4种颜色（用空格分隔），或输入“答案”查看正确答案：").strip().split()
        
        # 检查玩家是否想提前结束游戏
        if len(guess) == 1 and guess[0].lower() in ['答案', '退出']:
            print("你选择提前结束游戏。")
            print("正确的密码是：", secret_code)
            break

        # 检查输入是否有效
        if len(guess) != 4 or any(color not in COLORS for color in guess):
            print("输入无效，请确保输入4种不同的颜色，且颜色在可选范围内。")
            attempts -= 1  # 不消耗尝试次数
            continue

        if len(set(guess)) != 4:
            print("输入无效，颜色不能重复。")
            attempts -= 1  # 不消耗尝试次数
            continue

        feedback = get_feedback(secret_code, guess, mode)
        display_feedback(guess, feedback, mode)

        if guess == secret_code:
            print("恭喜你，猜对了！")
            break
    else:
        if max_attempts != float('inf'):  # 如果不是无限次数模式
            print(f"\n很遗憾，你没有在 {max_attempts} 次尝试内猜出密码。")
        show_answer = input("是否查看正确答案？（是/否）：").strip().lower()
        if show_answer == '是':
            print("正确的密码是：", secret_code)
        else:
            print("游戏结束，下次再来挑战吧！")

if __name__ == "__main__":
    main()
