def pprint(query, cur):

    # query : select statements
    # cur   : conn.cursor()

    res = cur.execute(query).fetchall()

    columns = [desc[0] for desc in cur.description]
    print("\t".join(columns))
    
    for record in res:
        print("\t".join(map(str, record)))


def execute_sql(filename, cur):

    # filename  : .sql file path
    # cur       : conn.cursor()

    q = 0

    with open(filename, 'r', encoding='utf-8') as f:
        script = f.read()
    

    commands = script.split(';')

    # print(commands)
    
    for command in commands:
        command = command.strip()
        if command:
            cur.execute(command)
            q+=1
            print(f"Executed query : {q}")
