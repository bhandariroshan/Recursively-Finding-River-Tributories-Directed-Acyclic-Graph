import csv
loop_count = 0


def extract(spamreader, initial_row):
    initial_x, initial_y = float(initial_row[6]), float(initial_row[7])
    global loop_count
    tributaries = [initial_row]
    for count, row in enumerate(spamreader):
        if count == 0:
            continue
        end_x = float(row[10])
        end_y = float(row[11])
        if initial_x == end_x and initial_y == end_y:
            tributaries.extend(extract(spamreader, row))
    return tributaries


def get_start(spamreader, x, y):
    for count, row in enumerate(spamreader):
        if count == 0:
            continue
        start_x = float(row[6])
        start_y = float(row[7])
        if start_x == x and start_y == y:
            return row

if __name__ == "__main__":
    init_x = -14979.6783
    init_y = 3480833.579
    tributaries = []
    with open('as_riv_15s_Clip.csv', 'r') as csvfile:
        spamreader1 = csv.reader(
            csvfile,
            delimiter=',',
            quotechar='|'
        )
        spamreader = [s for s in spamreader1]
        tributaries = extract(
            spamreader, get_start(spamreader, init_x, init_y)
        )
    with open('tributary.csv', 'w') as csvfile:
        spamwriter = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL
        )
        spamwriter.writerow(spamreader[0])
        for each_tributary in tributaries:
            spamwriter.writerow(each_tributary)
