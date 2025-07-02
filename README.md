# WIP

## quicksftp

**Ephemeral SFTP server for quick, secure file sharing — no system users, no config. Just run and go.**

## Design Goal

A single-command, temporary cross-platform SFTP server that:
- Creates an in-memory user
- Exposes a single directory for SFTP access
- Automatically shuts down after a specified time
- Displays logs for access and activity

### Example

```bash
# Expose ~/Downloads for 30 minutes
quicksftp ~/Downloads -t 30
```
Output
```bash
Username: tempuser
Password: ********
SFTP started on localhost:2022
SFTP URI: sftp://tempuser@localhost:2022
Session expires in 30m...

[10:45:00] tempuser connected
[10:45:08] tempuser downloaded test.txt
[11:15:00] Session expired, shutting down
```
