import click
import requests
import json

cli = click.Group()

BASE_URL = "http://127.0.0.1:5000"


def login(email, password):
    click.echo("Logging in..")
    response = requests.post(BASE_URL + "/login", json={"email": email, "password": password})
    if response.ok:
        click.echo("Successfully logged in!")
        return response.json()
    else:
        click.echo(str(response.json().get('message')))
        raise click.Abort()


def post_event_file(organization, workspace, event_file, token):
    click.echo("Updating the event file...")
    json_data = {
        'workspace_name': workspace,
        'organization_name': organization,
        'event_file': event_file
    }
    response = requests.post(BASE_URL + "/event_file", json=json_data,
                             headers={'Authorization': 'Bearer {}'.format(token)})
    if response.ok:
        click.echo("Successfully updated the event file!")
        return True
    else:
        click.echo(str(response.json().get('message')))
        raise click.Abort()


@cli.command()
@click.argument('event_file', type=click.File())
@click.option('-e', type=str, help="Your email")
@click.option('-p', type=str, help="Your password")
@click.option('-w', type=str, help="Your workspace name")
@click.option('-o', type=str, help="Your organization name")
def load(event_file, e, p, w, o):
    event_file_content = json.loads(event_file.read())

    token = login(e, p)
    post_event_file(o, w, event_file_content, token)
