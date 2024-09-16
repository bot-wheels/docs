## Working with the Repository

We use **Git Flow** to manage our development process, ensuring a structured and efficient workflow. For more details, refer to this [Git Flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/).

### Branches

- **Main Branch**: The main branch (`main`) holds the stable version of the project. Only key team members (me and Dawid) can merge into the `main` branch unless otherwise specified.
  
- **Development Branch**: The development branch (`develop`) is where active development happens. All feature branches are created from `develop` and merged back into it when a feature is completed. Only Dawid and I are authorized to merge into `develop` as well.

### Feature Branches

When starting a new feature, create a branch from `develop`:

```sh
git checkout develop
git pull origin develop
git checkout -b feature/my-new-feature
```

All feature branches should be named using the following pattern: `feature/<description-of-feature>`.

### Merging

Only authorized team members (Jakub C. and Dawid W.) can merge changes into `main` and `develop`. You can work on a feature branch, but a pull request must be reviewed before merging.

### Commit Guidelines

To track progress, it is important to commit frequently, ideally every day. Use the [Gitmoji](https://gitmoji.dev/) convention to make commit messages more descriptive. For example:

- 🚧 `:construction:` for work in progress.
- ✨ `:sparkles:` for introducing a new feature.
- 🐛 `:bug:` for fixing a bug.

If a task is still in progress, use the 🚧 emoji so that it’s clear the feature is incomplete.

Here’s an example of a commit message:

```sh
git commit -m ":sparkles: Add new feature for calculating goals"
```