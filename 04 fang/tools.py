import easygui

schedules = []


def show_schedule():
    schedules_s = []
    str = " | "

    for i in range(len(schedules)):
        schedules_s.append(str.join(schedules[i]))

    re = easygui.choicebox(msg="show all your shchedules:",
                           title="shchedules",
                           choices=schedules_s,
                           )


def new_schedule():
    # 添加新日程
    s_list = easygui.multenterbox(msg="enter your new schedule:",
                                  title="creat",
                                  fields=["time", "place", "event"]
                                  )
    if s_list != None:
        schedules.append(s_list)

    show_schedule()


def search_schedule():
    re = easygui.enterbox(msg='',
                          title="change schedules: enter the time: ",
                          default="000")

    i = 0

    for find in schedules:
        if find[1] == re:
            choice = easygui.buttonbox(msg="what do u want to do?",
                                       title="choice",
                                       choices=["change", "delete"])
            if choice == "change":
                change_schedule(i)
            elif choice == "delete":
                delete_schedule(i)
            else:
                easygui.msgbox("incalid operation")
            break
        if i == len(schedules):
            easygui.msgbox("no found...")
        i = i + 1


def change_schedule(i):
    schedules[i] = easygui.multenterbox(msg="enter your new schedule:",
                                        title="creat",
                                        fields=["time", "place", "event"]
                                        )
    show_schedule()


def delete_schedule(i):
    schedules.pop(i)
    show_schedule()