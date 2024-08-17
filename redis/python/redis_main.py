import redis

def list_keys(pattern: str) -> list:
    keys_list = [key.decode('utf-8') for key in r.keys(pattern=pattern)]
    return keys_list
    
def list_keys_efficient(pattern: str) -> list:
    cursor = 0
    keys_list = list()

    while True:
        cursor, keys = r.scan(cursor=cursor, match=pattern)
        keys_list.extend(keys)

        if cursor == 0:
            break
    
    return [key.decode('utf-8') for key in keys_list]

def member_count(key):
    key_type = r.type(key).decode('utf-8')

    if key_type == 'zset':
        return r.zcard(key)

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=7379, db=0)
    # print(list_keys_efficient('*'))

    queue_key = 'conductor_queues.test.QUEUE._deciderQueue.c'
    print(f'Total members in {queue_key}: {member_count(queue_key)}')
