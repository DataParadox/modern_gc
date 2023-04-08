import sys
import argparse
import os
import wget
import subprocess
import logging


logger = logging.getLogger(__name__)

def benchmark_download(args):
    if args.b_suite == "dacapo":
        url = "https://netix.dl.sourceforge.net/project/dacapobench/9.12-bach-MR1/dacapo-9.12-MR1-bach.jar"
    elif args.b_suite == "renaissance":
        url = "https://github.com/renaissance-benchmarks/renaissance/releases/download/v0.14.2/renaissance-mit-0.14.2.jar"
    downloaded_benchmark = wget.download(url)
    return downloaded_benchmark

def create_shell_file(args, loaded_benchmark):
    if args.varying_heap == False:  
        dir_  = args.b_suite+"_"+args.benchmark

        start_ = "benchmark="+args.benchmark+"\nmkdir "+dir_

        serial_gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseSerialGC -Xlog:gc*:file=serial_gc_"+args.benchmark+".log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv serial_gc_"+args.benchmark+".log "+dir_
        parallel_gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseParallelGC -Xlog:gc*:file=parallel_gc_"+args.benchmark+".log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv parallel_gc_"+args.benchmark+".log "+dir_
        zgc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseZGC -Xlog:gc*:file=zgc_"+args.benchmark+".log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv zgc_"+args.benchmark+".log "+dir_
        g1gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -Xlog:gc*:file=g1gc_"+args.benchmark+".log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv g1gc_"+args.benchmark+".log "+dir_
        epsilon_gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseEpsilonGC -Xlog:gc*:file=epsilon_gc_"+args.benchmark+".log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv epsilon_gc_"+args.benchmark+".log "+dir_

        shell_text = start_+"\n"+serial_gc+"\n"+parallel_gc+"\n"+zgc+"\n"+g1gc+"\n"+epsilon_gc

    else:
        heap_ = "(512"
        iterator = 512
        while iterator < args.max_heap:
            iterator = iterator * 2
            heap_ = heap_+" "+str(iterator)
        heap = heap_+")"



        dir_  = args.b_suite+"_"+args.benchmark

        start_ = "benchmark="+args.benchmark+"\nmkdir "+dir_+"\ndeclare -a heap_size="+heap_+"\nfor size in \"$heap_size[@]}\"\ndo\n"

        serial_gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseSerialGC -Xmx${size}M -Xlog:gc*:file=serial_gc_"+args.benchmark+"_${size}.log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv serial_gc_"+args.benchmark+"_${size}.log "+dir_
        parallel_gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseParallelGC -Xmx${size}M -Xlog:gc*:file=parallel_gc_"+args.benchmark+"_${size}.log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv parallel_gc_"+args.benchmark+"_${size}.log "+dir_
        zgc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseZGC -Xmx${size}M -Xlog:gc*:file=zgc_"+args.benchmark+"_${size}.log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv zgc_"+args.benchmark+"_${size}.log "+dir_
        g1gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -Xmx${size}M -Xlog:gc*:file=g1gc_"+args.benchmark+"_${size}.log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv g1gc_"+args.benchmark+"_${size}.log "+dir_
        epsilon_gc = "java -XX:+UnlockExperimentalVMOptions -XX:+UseEpsilonGC -Xmx${size}M -Xlog:gc*:file=epsilon_gc_"+args.benchmark+"_${size}.log -jar "+loaded_benchmark+" "+args.benchmark+"\nmv epsilon_gc_"+args.benchmark+"_${size}.log "+dir_

        shell_text = start_+"\n"+serial_gc+"\n"+parallel_gc+"\n"+zgc+"\n"+g1gc+"\n"+epsilon_gc+"\ndone"

    with open("temp.sh", "w") as f:
        f.write(shell_text)
    return "temp.sh"

def run_shell_file(shell):
    process = subprocess.Popen(['cmd', '/c', shell], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    print(output.decode("utf-8"))
    print(error.decode("utf-8"))

def delete_file(file):
    os.remove(file)


def main(args):

    loaded_benchmark = benchmark_download(args)
    shell = create_shell_file(args, loaded_benchmark)
    run_shell_file(shell)
    delete_file(shell)
    delete_file(loaded_benchmark)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--b_suite", type=str, help="Evaluation benchmark suite")
    parser.add_argument("--benchmark", type=str, help="Evaluation benchmark")
    parser.add_argument("--max_heap", type=int, default=512, help="Maximum heap size (in power of 2 and greater than 512 MB)")
    parser.add_argument("--varying_heap", type=bool, default=False, help="Varying heap size")

    args, _ = parser.parse_known_args()
    main(args)
