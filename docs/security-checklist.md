# Security Review Checklist

## Purpose
This checklist helps Team 05 review security and privacy risks before merging pull requests.

## 1. Secrets and Credentials
- [ ] No real API keys, passwords or access tokens are committed.
- [ ] `.env` files and local credentials are excluded from Git.
- [ ] `.env.example` contains placeholders only.
- [ ] No credentials appear in screenshots, logs or documentation.

## 2. Personal Data
- [ ] No student IDs, personal phone numbers or private email addresses are exposed without authorization.
- [ ] Test datasets use safe sample data.
- [ ] Logs do not expose sensitive personal information.
- [ ] Only necessary information is collected or displayed.

## 3. Code and Dependencies
- [ ] Input handling has been reviewed.
- [ ] Error messages do not expose sensitive internal information.
- [ ] New dependencies are justified and reviewed.
- [ ] Debug statements do not print secrets.

## 4. Pull Request Security Review
- [ ] The changed files have been inspected.
- [ ] Automated tests and relevant manual checks are recorded.
- [ ] No unexpected files or large data dumps are included.
- [ ] AI-generated content has been reviewed and disclosed where applicable.
- [ ] Security-related comments are resolved before approval.

## 5. Responding to Exposed Secrets
1. Stop merging the affected pull request.
2. Inform the Tech Lead or appropriate project maintainer.
3. Revoke or rotate the exposed credential immediately.
4. Remove the credential from the code and assess any exposure in Git history.
5. Review logs, documentation and dependent services for additional exposure.
6. Verify that replacement credentials are stored securely.

## How to Use
Before approving a pull request, the reviewer should inspect the code changes, use this checklist, and leave specific comments for any unresolved risk. An unresolved critical security finding must block approval.

## Note
The sample office records in this repository are demonstration data and must not be treated as verified official university information.
