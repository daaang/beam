User stories
============

Maybe not precisely or anything. I just want to write down how I expect
to use this, and what I expect it to do. Call it what you want.

Tasks and estimates
-------------------

### Create a task ###

When I add a task, I should be required to enter a brief (~50char)
description of the task. I should have the opportunity to either enter a
three-number estimate in terms of tomatoes or to begin adding sub-tasks.

### Update a task ###

#### Relational management ####

I should be able to add children to parent tasks, and I should be able
to split leaf tasks into multiple children. If there are no existing
tomatoes, then this is trivial. If there are tomatoes, then I'm not sure
the best way to handle it, since part of my goal is to track my
estimates.

Maybe parent tasks can have optional three-number estimates? If I leave
them out, then they'll default to sums of their components.

I should also be able to assign orphaned tomatoes to tasks. Although
this technically counts as updating a tomato, it should be presented as
modifying the task.

#### Other modifications ####

I should of course be able to modify the description, the estimate, and
the completion boolean.

### Delete a task ###

I should be able to delete a task, and it should appear painless.

I don't know how best to handle its tomatoes.

If it's the only child of a parent, then its estimate and completion
status should be copied to its parent (which becomes a leaf).

### Read tasks ###

#### Tables of tasks ####

I should be able to retrieve tabular data on tasks and their estimates.
I should be able to include/exclude tasks with implicit (i.e. summed)
estimates, and I should be able to view completed tasks, incomplete
tasks, or both.

The data should have these columns: actual, best, expected, worst, and
description. Optionally, it could include a sixth boolean column showing
whether the task is complete. I should be able to decide whether
composite tasks have blank estimates or show their generated estimates.

#### Analysis of estimate accuracy ####

I should also be able to ask for an accuracy breakdown of my X
most-recent estimates. This will ignore any incomplete tasks as well as
implicit estimates. Other than that, it should give me four counts:
total tasks looked at, tasks completed before best-case, tasks completed
before expected-case, and tasks completed after worst-case.

#### Translate estimate into days ####

I should be able to select an as-of-yet uncompleted task, provide a
percentage of my time I'm willing to spend on it, and I should receive
some in-english three-number estimates in days, weeks, or months
(alongside actual ETA dates) for each number.

It should also tell me how many tomatoes/workday its assuming in its
calculations.

This should depend on a tomato-read operation to determine how many
tomatoes I can count on in a day.

Tomatoes
--------

### Create a tomato ###

Tomatoes are created with timestamps, and I should have the option of
assigning the tomato to an incomplete task. We're talking about data
here, so this is separate from the interface, which would also handle
such as switching music to white noise, setting "away" on slack, etc.

Therefore, it's more like, tomatoes will be given timestamps at creation
and must also include (possibly blank) descriptions. They may also
include the id of the task they apply to.

They can apply to a parent task directly, although I shouldn't do this
if I can avoid it.

### Delete a tomato ###

Why not?

### Update a tomato ###

I should be able to reassign it to another task (or to no task), change
the description, and change the timestamp. Why not?

### Read tomatoes ###

The only read operation I actually expect to do (other than stuff like
"get a count of all tomatoes belonging to this task") is to get a total
count of tomatoes in the past X days.

When I do that, I'll ignore all days with a count of zero tomatoes. So,
if I say 10 days, it'll automatically ignore any days in which I was
vacationing or weekending. It'll also ignore any actual workdays in
which I accomplished zero tomatoes, but I've deemed this acceptable.

It should return the date of how far back it had to go, how many days
ago it's calling that (probably 10), how many days ago it actually is
(ideally 14), and how many tomatoes were accomplished since that date.

Any fractions based on that data can be figured out by the client.
