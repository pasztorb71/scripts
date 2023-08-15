import multiprocessing
import subprocess


def parallel_run(gitlist, proc_to_run, *args):
    return_dict = get_return_dict()
    jobs = []
    for git in gitlist:
        p = multiprocessing.Process(target=proc_to_run, args=(git, return_dict, *args))
        jobs.append(p)
        p.start()
    wait_until_end(jobs)
    return return_dict


def _mproc_multiple_commands(git, return_dict, commands):
    out = []
    err = []
    for cmd in commands:
        #print('cmd /u /c git -C ' + git.base +'/' + git.repo +' '+cmd)
        proc=subprocess.Popen('cmd /u /c git -C ' + git.base +'/' + git.repo +' '+cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out.append(proc.stdout.read().decode('utf-8'))
        e = proc.stderr.read().decode('utf-8')
        if any(x in e for x in ['error:', 'Aborting']):
            err.append(e)
    return_dict[git.repo] = {'stdout': out, 'stderr': err}


def get_return_dict():
    manager = multiprocessing.Manager()
    return manager.dict()


def wait_until_end(jobs):
    for job in jobs:
        job.join()