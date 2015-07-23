# MelbDjango School - Lesson Two

## Displaying the class slides

Install reveal-md with npm and use that to display the class slides.

```
    npm install -g reveal-md

    cd slides
    reveal-md CLASS.md --theme melbdjango
```

## Homework Checklist

If you did the homework [last week][lesson-one], you should already have a virtualenv that you can use this week.

- [ ] [Fork this repository][gh-fork]
- [ ] Clone the repo to your own machine
- [ ] Normalise the model we created in class by creating new [Django models][dj-models] that better express the
      relationships. You'll need to add ForeignKey relationships between your models and our existing one.
- [ ] Update `admin.py` so all your new models show

[gh-fork]: https://help.github.com/articles/fork-a-repo/
[lesson-one]: https://github.com/melbdjango/lesson-one/
[dj-models]: https://docs.djangoproject.com/en/1.8/topics/db/models/
[dj-fk]: https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey
