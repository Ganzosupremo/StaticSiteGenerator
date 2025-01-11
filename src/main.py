import os
import shutil

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            copy_directory(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {dst_path}")

def main():
    src_dir = 'static'
    dst_dir = 'public'
    copy_directory(src_dir, dst_dir)


if __name__ == "__main__":
    main()