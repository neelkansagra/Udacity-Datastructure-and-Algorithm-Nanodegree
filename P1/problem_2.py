import os

def find_all_files(suffix,path,list_of_files):
    list_of_items_inside_dir = os.listdir(path)         #list of all files and directories inside a given directory
    
    for item in list_of_items_inside_dir:
        new_path = os.path.join(path,item)
        
        if os.path.isfile(new_path):                    #if the new path is a file
            
            if item.endswith(suffix):                   #if the suffix of the file matches then add it to the list
                list_of_files.append(new_path)
 
        elif os.path.isdir(new_path):                   #if the new path is a directory then explore the directory
            find_all_files(suffix,new_path,list_of_files)

    return list_of_files


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix=='':
        return []
    return find_all_files(suffix,path,[])


# Normal Cases:
print(find_files(suffix='c', path='.'))
# ['.\\testdir\\testdir\\subdir1\\a.c', '.\\testdir\\testdir\\subdir3\\subsubdir1\\b.c', '.\\testdir\\testdir\\subdir5\\a.c', '.\\testdir\\testdir\\t1.c']

print(find_files(suffix='h', path='.'))
# ['.\\testdir\\testdir\\subdir1\\a.h', '.\\testdir\\testdir\\subdir3\\subsubdir1\\b.h', '.\\testdir\\testdir\\subdir5\\a.h', '.\\testdir\\testdir\\t1.h']

print(find_files(suffix='.gitkeep', path='.'))
# ['.\\testdir\\testdir\\subdir2\\.gitkeep', '.\\testdir\\testdir\\subdir4\\.gitkeep']

print(find_files(suffix='z', path='.'))
# []

# Edge Cases:
print(find_files(suffix='', path='.'))
# []
