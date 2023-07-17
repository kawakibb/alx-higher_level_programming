#include "lists.h"

/**
 * reverse_listint - linked list reversed
 * @head: first node in the list
 * Return: first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *cur = *head;
	listint_t *next = NULL;

	while (cur)
	{
		next = cur->next;
		cur->next = prv;
		prv = cur;
		cur = next;
	}

	*head = prv;
}

/**
 * is_palindrome - checks palindrom in linked list
 * @head: linked list doubl ponter
 *
 * Return: 1 success, 0 fail
 */
int is_palindrome(listint_t **head)
{
	listint_t *slower = *head, *faster = *head, *tmp = *head, *dp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		faster = faster->next->next;
		if (!faster)
		{
			dp = slower->next;
			break;
		}
		if (!faster->next)
		{
			dp = slower->next->next;
			break;
		}
		slower = slower->next;
	}

	reverse_listint(&dp);

	while (dp && tmp)
	{
		if (tmp->n == dp->n)
		{
			dp = dp->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dp)
		return (1);

	return (0);
}
