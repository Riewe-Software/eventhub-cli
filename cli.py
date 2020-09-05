import click
import requests
import json

cli = click.Group()


def login(email, password, endpoint):
    click.echo("Logging in..")
    response = requests.post(endpoint + "/login", json={"email": email, "password": password})
    if response.ok:
        click.echo("Successfully logged in!")
        return response.json()
    else:
        click.echo(str(response.json().get('message')))
        raise click.Abort()


def post_signup(email, password, endpoint):
    click.echo("Signing up..")
    response = requests.post(endpoint + "/user", json={"email": email, "password": password})
    if response.ok:
        click.echo("Successfully signed up!")
        return response.json()
    else:
        click.echo(str(response.json().get('message')))
        raise click.Abort()


def post_event_file(organization, workspace, event_file, token, endpoint):
    click.echo("Updating the event file...")
    json_data = {
        'workspace_name': workspace,
        'organization_name': organization,
        'event_file': event_file
    }
    response = requests.post(endpoint + "/event_file", json=json_data,
                             headers={'Authorization': 'Bearer {}'.format(token)})
    if response.ok:
        click.echo("Successfully updated the event file!")
        return True
    else:
        click.echo(str(response.json().get('message')))
        raise click.Abort()


@cli.command()
@click.argument('email', type=str)
@click.argument('password', type=str)
@click.option('--endpoint', type=str, help="Eventhub endpoint", default="https://eventhub-backend-dev.herokuapp.com/")
def signup(email, password, endpoint):
    post_signup(email, password, endpoint)


@cli.command()
@click.argument('event_file', type=click.File())
@click.option('-e', '--email', type=str, help="Your email")
@click.option('-p', '--password', type=str, help="Your password")
@click.option('-w', '--workspace', type=str, help="Your workspace name")
@click.option('-o', '--organization', type=str, help="Your organization name")
@click.option('--endpoint', type=str, help="Eventhub endpoint", default="https://eventhub-backend-dev.herokuapp.com/")
def push(event_file, email, password, workspace, organization, endpoint):
    event_file_content = json.loads(event_file.read())

    token = login(email, password, endpoint)
    post_event_file(organization, workspace, event_file_content, token, endpoint)
