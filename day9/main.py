def read_input(input_file_dir):
    lines = open(input_file_dir, 'r')
    lines = [line.strip() for line in lines]
    return lines[0]

def expand_disk(comapact_disk):
    disk = []
    idx = 0
    for pos, node in enumerate(comapact_disk):
        if pos % 2 == 0:
            for times in range(int(node)):
                disk.append(idx)
            idx += 1
        else:
            for times in range(int(node)):
                disk.append('.')
    return disk

def reallocate_files(disk, right):
    while right >= 0 and disk[right] == '.':
        right = right - 1
    if right >= 0:
        file = disk[right]
        disk[right] = '.'
        return file, right
    return 0, -1

def calculate_checksum(disk):
    left = 0
    right = len(disk) - 1
    space = []
    checksum = 0
    while left < right:
        if disk[left] == '.' or len(space) > 0 and space[0] < left:
            space.append(left)
            if right >= 0:
                file, new_right = reallocate_files(disk, right)
                right = new_right
                if len(space) > 0:
                    space_location = space.pop(0)
                    disk[space_location] = file
                    checksum += file * space_location
                else:
                    disk[left] = file
                    checksum += file * left
        else:
            checksum += disk[left] * left
        left += 1
    return checksum

harddisk = read_input('./input.txt')
print(calculate_checksum(expand_disk(harddisk)))

# Part 2

def expand_disk_v2(comapact_disk):
    disk = []
    space = {}
    idx = 0
    for pos, node in enumerate(comapact_disk):
        if pos % 2 == 0:
            for times in range(int(node)):
                disk.append(idx)
            idx += 1
        else:
            for times in range(int(node)):
                disk.append('.')
    return disk

def reallocate_files_v2(disk):
    right = len(disk) - 1
    while right >= 0:
        if disk[right] != '.':
            file = disk[right]
            file_size = 0
            while disk[right] == file:
                file_size += 1
                disk[right] = '.'
                right -= 1
            left = 0
            space = ''
            while left < right and file_size > 0:
                if disk[left] == '.':
                    space = space + '.'
                    if len(space) == file_size:
                        for i in range(file_size):
                            disk[left-i] = file
                        file_size = 0
                else:
                    space = ''
                left += 1
            if file_size >0:
                right += 1
                for j in range(file_size):
                    disk[right+j] = file
                right -= 1
        else:
            right -= 1
    return disk

def calculate_checksum_v2(disk):
    disk = reallocate_files_v2(disk)
    checksum = 0
    print(disk)
    for i, file in enumerate(disk):
        if file != '.':
            checksum += file * i
    return checksum


harddisk = read_input('./input.txt')
print(calculate_checksum_v2(expand_disk_v2(harddisk)))