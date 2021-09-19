from pathlib import Path
import sys

def run():

	try:
		user_input = sys.argv[1]
	except:
		print('Please pass a directory name')
		sys.exit(1)

	directory_name = Path(user_input)
	dotfiles_path = directory_name.resolve()
	home_dir = Path.home()
	current_dir = Path.cwd()

	def sync_dotfiles():
		for y in dots_dirs:
			dir_in = Path(y)
			dir_name = dir_in.relative_to(dotfiles_path)
			dir_out = home_dir / dir_name
			check_dir(dir_out)
		for x in dots_files:
			dot_in = Path(x)
			dot_name = dot_in.relative_to(dotfiles_path)
			dot_out = home_dir / dot_name
			check_file(dot_out)
			make_links(dot_in, dot_out)

	def make_links(dotin, dotout):
		dotout.symlink_to(dotin)	

	def check_file(thefile):
		if thefile.is_symlink():
			thefile.unlink()
		else: pass
		if thefile.is_file():
			rename_old(thefile)
		else: pass

	def check_dir(thedir):
		if thedir.is_dir():
		    pass
		else:
		    thedir.mkdir(parents=True, exist_ok=True)

	def rename_old(thefile):
		fullname = thefile
		fname = thefile.stem
		fsuffix = thefile.suffix
		fdir = thefile.parents[0]
		new_name = Path(fname + '_old' + fsuffix)
		path_old = fdir / new_name
		fullname.rename(path_old)

	def check_exist(usrdir):
		# if usrdir.exists():
		if usrdir.is_dir():
		    return True    
		else:
		    return False

	# def run():
	if check_exist(dotfiles_path):
		dots_all = dotfiles_path.rglob('*')
		dots_list = [x for x in dots_all]
		dots_files = [x for x in dots_list if x.is_file()]
		dots_dirs = [x for x in dots_list if x.is_dir()]
		sync_dotfiles()
		print("Synced Dotfiles")
	else:
		print("invalid Directory")

run()

