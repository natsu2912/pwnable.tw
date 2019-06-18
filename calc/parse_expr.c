signed int __cdecl parse_expr(int a1, _DWORD *a2)
{
  int v2; // ST2C_4
  int v4; // eax
  int v5; // [esp+20h] [ebp-88h]
  int i; // [esp+24h] [ebp-84h]
  int v7; // [esp+28h] [ebp-80h]
  char *s1; // [esp+30h] [ebp-78h]
  int v9; // [esp+34h] [ebp-74h]
  char s[100]; // [esp+38h] [ebp-70h]
  unsigned int v11; // [esp+9Ch] [ebp-Ch]

  v11 = __readgsdword(0x14u);
  v5 = a1;
  v7 = 0;
  bzero(s, 0x64u);
  for ( i = 0; ; ++i )
  {
    if ( (unsigned int)(*(char *)(i + a1) - 48) > 9 )
    {
      v2 = i + a1 - v5;
      s1 = (char *)malloc(v2 + 1);
      memcpy(s1, v5, v2);
      s1[v2] = 0;
      if ( !strcmp(s1, "0") )
      {
        puts("prevent division by zero");
        fflush(stdout);
        return 0;
      }
      v9 = atoi(s1);
      if ( v9 > 0 )
      {
        v4 = (*a2)++;
        a2[v4 + 1] = v9;
      }
      if ( *(_BYTE *)(i + a1) && (unsigned int)(*(char *)(i + 1 + a1) - 48) > 9 )
      {
        puts("expression error!");
        fflush(stdout);
        return 0;
      }
      v5 = i + 1 + a1;
      if ( s[v7] )
      {
        switch ( *(char *)(i + a1) )
        {
          case '%':
          case '*':
          case '/':
            if ( s[v7] != 43 && s[v7] != 45 )
            {
              eval(a2, s[v7]);
              s[v7] = *(_BYTE *)(i + a1);
            }
            else
            {
              s[++v7] = *(_BYTE *)(i + a1);
            }
            break;
          case '+':
          case '-':
            eval(a2, s[v7]);
            s[v7] = *(_BYTE *)(i + a1);
            break;
          default:
            eval(a2, s[v7--]);
            break;
        }
      }
      else
      {
        s[v7] = *(_BYTE *)(i + a1);
      }
      if ( !*(_BYTE *)(i + a1) )
        break;
    }
  }
  while ( v7 >= 0 )
    eval(a2, s[v7--]);
  return 1;
}