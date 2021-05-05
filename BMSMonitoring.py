bms_readings = [3, 3, 5, 4, 10, 11, 12]
range_list = []
unique_sequences = []
all_sequences = []
count_dict = {}

def isValidInput(list):
    if list is None:
        return False
    else:
        return True
      
def getRangeCount(bms_readings):
    max_value = max(bms_readings)
    min_value = min(bms_readings)
    range_list = getRangeList(min_value,max_value)
    paired_sequences = getPairedSequence(range_list)
    return getSequenceCount (bms_readings, paired_sequences)

def getRangeList(min,max):
  for i in range(min,max+1):
    range_list.append(i)
  return range_list

def getPairedSequence(range_list):
    for i in range (0, len(range_list)-2,3):
        for j in range (3):
            if not i > len(range_list) - 3:
                unique_range = [range_list[i],range_list[i+1],range_list[i+2]]
                i = i + 1
                all_sequences.append(unique_range)
    return all_sequences

def getSequenceCount(bms_readings, paired_sequences):
    for sequence in paired_sequences:
        minval = sequence[0]
        maxval = sequence[2]
        range_string = str(minval) + "-" + str(maxval)
        count = 0
        if set(sequence).issubset(bms_readings):
            for i in bms_readings:
                if i in sequence:
                    count += 1              
            count_dict[range_string] = str(count)      
    return count_dict
