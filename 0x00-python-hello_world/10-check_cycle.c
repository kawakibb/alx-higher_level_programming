#include "lists.h"

/**
 * check_cycle - checks the linked_list if it contains a cycle or not
 * @list: linked list were we check
 * Return: 1 if succes, 0 if it fail
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *c = list;

	if (!list)
		return (0);

	while (s && c && c->next)
	{
		s = s->next;
		c = c->next->next;
		if (s == c)
			return (1);
	}

	return (0);
}
