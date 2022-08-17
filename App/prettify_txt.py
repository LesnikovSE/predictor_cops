def clear_text():
    f = open('whatsapp_speech.txt', 'r', encoding='utf-8')
    main_list = []
    for row in f.readlines():
        r = row[1:-3].split(', ')
        r2 = []
        for i in r:
            r2.append(i[1:-1])
        main_list.append(r2)
    return main_list
