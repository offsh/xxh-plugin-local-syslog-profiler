remote_origin = f"{host_xxh_home}/.local/share/xonsh/syslog/shell_profiler.log"
local_destination = "/tmp/xxh-syslog-profiler-tmp"

bash_wrap_begin = "bash -c 'shopt -s dotglob && "
bash_wrap_end = "'"

shell_build_dir = self.local_xxh_home / '.xxh/shells' / self.shell / 'build'

copy_method = None
if opt.copy_method:
    copy_method = opt.copy_method
if self.local:
    copy_method = 'cp'

if copy_method == 'rsync' or (copy_method is None and which('rsync') and host_info['rsync']):
    self.eprint('Retrieving remote logs.')

    rsync = "rsync {ssh_arg_v} -e \"{sshpass} {ssh} {ssh_arg_v} {ssh_arguments}\" {arg_q} -az {progress} --cvs-exclude --include core ".format(
        host_xxh_home=host_xxh_home,
        sshpass=A(self.sshpass),
        ssh=A(self.ssh_command),
        ssh_arg_v=('' if self.ssh_arg_v == [] else '-v'),
        ssh_arguments=A(self.ssh_arguments, 0, 3),
        arg_q=A(arg_q),
        progress=('' if self.quiet or not self.verbose else '--progress')
    )

    self.S("{bb}{rsync} {host}:{remote_origin} {local_destination} 1>&2{be}".format(
        bb=bash_wrap_begin,
        be=bash_wrap_end,
        rsync=rsync,
        host=A(host),
        local_destination=local_destination,
        remote_origin=remote_origin
    ))
elif copy_method == 'scp' or (copy_method is None and which('scp') and host_info['scp']):
    self.eprint('Retrieving remote logs.')
    scp = "{sshpass} {scp_command} {ssh_arg_v} {ssh_arguments} -r -C {arg_q}".format(
        sshpass=A(self.sshpass),
        scp_command=A(self.scp_command),
        ssh_arg_v=A(self.ssh_arg_v),
        ssh_arguments=A(self.ssh_arguments, 0, 1),
        arg_q=A(arg_q)
    )

    self.S('{bb}{scp} {host}:{remote_origin} {local_destination} 1>&2{be}'.format(
        bb=bash_wrap_begin,
        be=bash_wrap_end,
        scp=scp,
        host=host,
        local_destination=local_destination,
        remote_origin=remote_origin
    ))
elif copy_method == 'skip':
    if self.verbose:
        self.eprint('Skip copying')
else:
    self.eprint('Please install rsync or scp!')

local_file = os.path.expanduser("~") + "/.local/share/xonsh/syslog/shell_profiler.log"

with open(local_destination, 'r') as tmp_file:
    with open(local_file, 'a+') as local_log:
        local_log.write(tmp_file.read())