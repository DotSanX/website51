from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

bd = {
  'contacts': [
    #{
    #  'name': "Максим Вершинин",
    #  'color': "#fccf05",
    #  'image': "static/image/teacher_in_sunglasses_with_guitar.jpeg",
    #  'description':
    #  "Преподаватель и идеолог этих величайших программистов, работающих над этим сайтом",
    #  'url_youtube': "https://www.youtube.com/channel/UChkWiGoytU_R_rl_ezGfJUA",
    #  'url_telegram': "https://t.me/wozborn",
    #  'url_vk': "https://vk.com/wozborn",
    #  'url_instagram': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    #  'url_discord': "https://discordapp.com/users/281838918532333580"
    #},
    #{
    #  'name': "билибоба",
    #  'color': "#ffffff",
    #  'image':
    #  "https://avatars.mds.yandex.net/i?id=b8518c5a96d7c03e0218f742b48a486b4cec19cf-10143943-images-thumbs&n=13",
    #  'description': "Пава пепе гима боди",
    #  'url_youtube': "https://www.youtube.com/watch?v=EE-xtCF3T94",
    #  'url_telegram': "https://www.youtube.com/watch?v=79v_C34h6YU",
    #  'url_vk': "https://www.youtube.com/watch?v=Fnbd5z8kJFk&t=1795s",
    #  'url_instagram': "https://www.youtube.com/watch?v=JJis0sld2cM",
    #  'url_discord': "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    #}
  ],
  "posts": [
    {
      "image": "https://hsbi.hse.ru/upload/articles/2021/700/machine-learning.jpg alt='Chat GPT думает как уничтожить человечество' width='550' height='350' class='border' ",
      "title": "Глубокое машинное обучение",
      "content": "<bold>Машинное обучение</bold> – это наука о разработке алгоритмов и     статистических моделей, которые компьютерные системы используют для выполнения задач без явных инструкций, полагаясь вместо этого на шаблоны и логические выводы. Компьютерные системы используют алгоритмы машинного обучения для обработки больших объемов статистических данных и выявления шаблонов данных."
    },
    {
      "image":
      "https://i.scdn.co/image/ab67616d0000b273d3fb156679ceb39d98ad5347 width='500' height ='500' class = border3"  ,
      "title":
      "Doxbin",
      "content":
      "<bold>Доксбин</bold> изначально был сайтом из Darknet, где публиковались найденные документы и другая информация о людях. То есть, в целом серьёзный сайт деанонеров. Теперь же он доступен и в обычном интернете. Только теперь это уже совсем другое место."
    },
    {
      "image":
      "https://www.it-courses.by/wp-content/uploads/2018/05/р1.png alt='language' width='500' height='500' class='border4'",
      "title":
      "Многогранность языков",
      "content":
      "Cейчас много языков програмирования. И что бы выбрать правильный, надо сначала определиться, с чем ты хочешь иметь дело. Например, сайт написан на HTML и CSS. Игры делаются на С++ и С+, а телеграмм боты, как на Python, так и на JavaScript"
    }
  ]
}


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/blog')
def blog():
  return render_template('blog.html', **bd)


@app.route('/contacts')
def contacts():
    conn = sqlite3.Connection("db.sqlite")
    cur = conn.cursor()

    cur.execute("""select name, description, image, color, url_youtube, url_telegram, url_vk, url_instagram, url_discord from contacts""")

    bd_contacts = { "contacts": []}
    for name, description, image, color, url_youtube, url_telegram, url_vk, url_instagram, url_discord in cur.fetchall():
      bd_contacts['contacts'].append({'name': name, 'description' : description, 'image' : image, 'color' : color, 'url_youtube' : url_youtube,'url_telegram' : url_telegram, 'url_vk' : url_vk, 'url_instagram' : url_instagram, 'url_discord' : url_discord})

    conn.close()

    return render_template("contacts.html", **bd_contacts )

@app.route('/blogsql')
def blogsql():
  conn = sqlite3.connect('db.sqlite')
  cur = conn.cursor()
  cur.execute("""select image, title, content from posts""")

  for image, title, content in cur.fetchall():
    bd['posts'].append({'image':image, 'title':title, 'content':content})
    
  conn.close()
  return render_template("blog.html", **bd)



@app.route('/contacts/add/', methods=['GET', 'POST'])
def contacts_add():
    print("contacts template rendered")
    if request.method == "GET":
      print("get is working")
    if request.method == "POST":
        print("post working")
        name = request.form.get('name')
        if name == "":
            context_warning = {
                'warning_type' : "Введите ваше имя!"
            }
            return render_template('contacts_warning_page.html', **context_warning)
        image = request.form.get('image')
        color = request.form.get('color')
        description = request.form.get('description')

        check_youtube = request.form.get('check_youtube')
        if check_youtube == None:
            url_youtube = None
        else: url_youtube = request.form.get('url_youtube')
        if check_youtube != None and url_youtube == "":
            context_warning = {
                'warning_type': "Неуказана используемая ссылка!"
            }
            return render_template('contacts_warning_page.html', **context_warning)

        check_telegram = request.form.get('check_telegram')
        if check_telegram == None:
            url_telegram = None
        else: url_telegram = request.form.get('url_telegram')
        if check_telegram != None and url_telegram == "":
            context_warning = {
                'warning_type': "Неуказана используемая ссылка!"
            }
            return render_template('contacts_warning_page.html', **context_warning)

        check_vk = request.form.get('check_vk')
        if check_vk == None:
            url_vk = None
        else: url_vk = request.form.get('url_vk')
        if check_vk != None and url_vk == "":
            context_warning = {
                'warning_type': "Неуказана используемая ссылка!"
            }
            return render_template('contacts_warning_page.html', **context_warning)

        check_instagram = request.form.get('check_instagram')
        if check_instagram == None:
            url_instagram = None
        else: url_instagram = request.form.get('url_instagram')
        if check_instagram != None and url_instagram == "":
            context_warning = {
                'warning_type': "Неуказана используемая ссылка!"
            }
            return render_template('contacts_warning_page.html', **context_warning)

        check_discord = request.form.get('check_discord')
        if check_discord == None:
            url_discord = None
        else: url_discord = request.form.get('url_discord')
        if check_discord != None and url_discord == "":
            context_warning = {
                'warning_type': "Неуказана используемая ссылка!"
            }
            return render_template('contacts_warning_page.html', **context_warning)

        username = request.form.get('username')
        if username == None:
            context_warning = {
                'warning_type': "Введите ваш никнейм!"
            }
            return render_template('contacts_warning_page.html', **context_warning)
        password = request.form.get('password')
        if password == None:
            context_warning = {
                'warning_type': "Введите ваш пароль!!"
            }
            return render_template('contacts_warning_page.html', **context_warning)
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute("""select exists(select username from contacts where username == ?)""", (username,))
        if (cur.fetchall()[0])[0] == 1:
            context_warning = {
                'warning_type': "Такое имя пользователя (никнейм) уже существует!"
            }
            return render_template('contacts_warning_page.html', **context_warning)
        conn = sqlite3.connect("db.sqlite")
        cur = conn.cursor()
        cur.execute("""insert into contacts (name,image,color,description,url_youtube,url_telegram,url_vk,url_instagram,url_discord,username,password) values (?,?,?,?,?,?,?,?,?,?,?)""",
        (name,image,color,description,url_youtube,url_telegram,url_vk,url_instagram,url_discord,username,password))
        conn.commit()
        conn.close()

        context_warning = {
                'warning_type': "Гига-бойчик добавлен"
            }
      #
        return render_template('contacts_warning_page.html', **context_warning)
    context_contacts = {
        "contacts_url": "/contacts/add/",
        "name": "ПрограммЁр", 
        "image": "",
        "color":"#ffffff",
        "description": 'У этого чувака нет истории, есть только путь... ',
        "url_youtube": "",
        "url_telegram": "",
        "url_vk": "",
        "url_instagram": "",
        "url_discord": "",
        "username": "",
        "password": ""
    }
    return render_template('contacts_add.html', **context_contacts, **bd )

  

@app.route('/contacts/edit')
def contacts_edit():
  conn = sqlite3.connect("db.sqlite")
  cur = conn.cursor()
  cur.execute("""select image, color, username from contacts""")
  bd_contacts_edit = { "contacts": []}
  for image, color, username in cur.fetchall():
    bd_contacts_edit['contacts'].append({'image' : image, 'color' : color, 'username' : username})
  conn.close()
  return render_template('contacts_edit.html', **bd_contacts_edit)

@app.route('/contacts/edit/<username>/', methods=['GET', 'POST'])
def contacts_edit_card(username = None ):
  conn = sqlite3.connect("db.sqlite")
  cur = conn.cursor()
  cur.execute("""select image, color, username from contacts""")
  bd_contacts_edit = { "contacts": []}
  for image, color, username in cur.fetchall():
    bd_contacts_edit['contacts'].append({'image' : image, 'color' : color, 'username' : username})
  conn = sqlite3.connect("db.sqlite")
  cur = conn.cursor()
  if request.method == "POST":
    name = request.form.get('name')
    if name == "":
      context_warning = {
        'warning_type' : "Введите ваше имя!"
      }
      return render_template('contacts_warning_page.html', **context_warning)
   
    image = request.form.get('image')
    color = request.form.get('color')
    description = request.form.get('description')
    check_youtube = request.form.get('check_youtube')
    if check_youtube == None:
        url_youtube = None
    else: url_youtube = request.form.get('url_youtube')
    if check_youtube != None and url_youtube == "":
        context_warning = {
            'warning_type': "Неуказана используемая ссылка!"
        }
        return render_template('contacts_warning_page.html', **context_warning)
    check_telegram = request.form.get('check_telegram')
    if check_telegram == None:
        url_telegram = None
    else: url_telegram = request.form.get('url_telegram')
    if check_telegram != None and url_telegram == "":
        context_warning = {
            'warning_type': "Неуказана используемая ссылка!"
        }
        return render_template('contacts_warning_page.html', **context_warning)
    check_vk = request.form.get('check_vk')
    if check_vk == None:
        url_vk = None
    else: url_vk = request.form.get('url_vk')
    if check_vk != None and url_vk == "":
        context_warning = {
            'warning_type': "Неуказана используемая ссылка!"
        }
        return render_template('contacts_warning_page.html', **context_warning)
    check_instagram = request.form.get('check_instagram')
    if check_instagram == None:
        url_instagram = None
    else: url_instagram = request.form.get('url_instagram')
    if check_instagram != None and url_instagram == "":
        context_warning = {
            'warning_type': "Неуказана используемая ссылка!"
        }
        return render_template('contacts_warning_page.html', **context_warning)
    check_discord = request.form.get('check_discord')
    if check_discord == None:
        url_discord = None
    else: url_discord = request.form.get('url_discord')
    if check_discord != None and url_discord == "":
        context_warning = {
            'warning_type': "Неуказана используемая ссылка!"
        }
        return render_template('contacts_warning_page.html', **context_warning)
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()
    cur.execute("""select exists(select (username, password) from contacts where (username == ? and password == ?))""", (username, password,))
    if (cur.fetchall()[0])[0] == 1:
      context_warning = {
        'warning_type': "Информация на карточке обновлена!"
      }
      cur.execute("""update contacts set name = ?, description = ?, color = ?, image = ?, url_youtube = ?, url_telegram = ?, url_vk = ?, url_instagram = ?, url_telegram = ? where username == ?;""",
      (name, description, color, image, url_youtube, url_telegram, url_vk,url_instagram, url_telegram, username,))
      return render_template('contacts_warning_page.html', **context_warning)
    else: 
      context_warning = {
        'warning_type': "Неверный логин или пароль!"
      }
      return render_template('contacts_warning_page.html', **context_warning)
    conn.close()
  return render_template('contacts_edit.html', **bd_contacts_edit)

# @app.route('/base_secret')
# def base_secret():
#   return render_template('base.html')


app.run(host='0.0.0.0', port=81)
'''Дорогой Даниил. Мне тебя очень жаль. Если тебе будет нужна поддержка, иди к белому другу. Он тебя никак другой поймет и обнимит'''
'''Дорогой дневник.. Мне не передать мои боли и страдания.. Каждый день я встаю в 6 часов утра чтобы позавтракать, пичистить зубы, пойти в школу, вернуться со школы и по новой.. Эти крысиннные бега мне надоели...'''
''' Настоящий программист всегда должен ложиться спать или в 1:28 или в 2:56... Ну, на крайний случай, в 5:12.
— А вставать в 10:24. Ну, на крайний случай, в 20:48.
А поясни шутку? Нет ;))))))
'''
'''И помните: Империя заботиться о вас!'''

#будующее наступило - мультиплеер в пайтоне...
#ждём когда добавят игровые режимы...
