import argparse
import pathlib
import yaml
from jinja2 import Environment, FileSystemLoader


parser = argparse.ArgumentParser()

parser.add_argument('yamlfile',
                       metavar='file.yml',
                       type=str,
                       help='YAML file for router config generation')

args = parser.parse_args()
file = pathlib.Path(args.yamlfile)

if not file.exists():
    print('File Not Found! Please check path and file name.')
    exit(1)
else:
    config = yaml.load(open(file),Loader=yaml.FullLoader)

    env = Environment(loader = FileSystemLoader('./templates/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('template.j2')

    for router in config.keys():
        output = 'output/' + router +'.config'
        with open(output, 'w') as f:
            f.write(template.render(config[router]))
        print(f'Configs was saved as {output}')



