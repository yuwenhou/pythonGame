import tools
import easygui

menu = ['create', 'show all', 'change', 'quit']

while 1:
    action = easygui.buttonbox(msg="          ************ welcome to schedule management system ***************",
                      title="schedule",
                      choices=menu,
                      default_choice=None,
                      cancel_choice=None,
                      callback=None,
                      run=True
                      )

    # 根据用户输入决定后续操作
    if action == 'create':
        tools.new_schedule()

    elif action == 'change':
        tools.search_schedule()

    elif action == 'show all':
        tools.show_schedule()

    elif action == "quit":
        easygui.msgbox("welcome to use schedule management system")
        break

    else:
        easygui.msgbox("please click again...")