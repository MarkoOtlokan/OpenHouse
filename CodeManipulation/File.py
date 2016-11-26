def insert_line(input_stream, pos, new_name, output_stream):
  inserted = False
  for line in input_stream:
    number, name = parse_line(line)
    if number == pos:
      print >> output_stream, format_line(number, new_name)
      inserted = True
    print >> output_stream, format_line(number if not inserted else (number + 1), name)

def parse_line(line):
  number_str, name = line.strip().split()
  return (get_number(number_str), name)

def get_number(number_str):
  return int(number_str.split('.')[0])

def format_line(number, name):
  return add_dot(number) + ' ' + name

def add_dot(number):
  return str(number) + '.'