# from pathlib import Path
# import sys

def run():

	from pathlib import Path
	import sys
	import subprocess

	home_dir = Path.home()
	current_dir = Path.cwd()
	dotfig_config = home_dir / ".config" / "dotfig" / "dotfig.txt"

	try:
		user_input = sys.argv[1]
	except:
		print('Please pass a directory name or command')
		sys.exit(1)

	if user_input == "sync":
		if dotfig_config.is_file():
			# directory_name = Path(user_input)
			dotfiles_path = Path(dotfig_config.read_text())
			# with open(dotfig_config, 'r') as f:
				# dotfiles_path = f.read()
				# dotfiles_path = directory_name.resolve()
		else:
			print("error no dotfig config file found, run dotfig command + path first to generate one")
			sys.exit(1)

	elif user_input == "push":
		if dotfig_config.is_file():
			dotfiles_path = dotfig_config.read_text()
			# cmdout = subprocess.run(['git', 'add', '.', '&&', 'git commit -m \'dotfig update\'', '&&', 'git push'], cwd=dotfiles_path, stdout=subprocess.PIPE).stdout.decode('utf-8')
			cmdout = subprocess.run(['git', 'add', '.'], cwd=dotfiles_path, stdout=subprocess.PIPE).stdout.decode('utf-8')
			print(cmdout)
			cmdout = subprocess.run(['git', 'commit', '-m', '\"dotfig update\"'], cwd=dotfiles_path, stdout=subprocess.PIPE).stdout.decode('utf-8')
			print(cmdout)
			cmdout = subprocess.run(['git', 'push'], cwd=dotfiles_path, stdout=subprocess.PIPE).stdout.decode('utf-8')
			print(cmdout)
			print("UPLOADED")
			sys.exit(1)	
		else:
			print("error no dotfig config file found, run dotfig command + path first to generate one, then run push to upload to your pre-configured github repo")
			sys.exit(1)	
	else:
		directory_name = Path(user_input)
		dotfiles_path = directory_name.resolve()
		if dotfig_config.is_file():
			dotfig_config.write_text(str(dotfiles_path))
		else:
			dotfig_parent = dotfig_config.parent
			dotfig_parent.mkdir(parents=True, exist_ok=True)
			dotfig_config.touch()
			dotfig_config.write_text(str(dotfiles_path))

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

# run()

